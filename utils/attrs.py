class Attr():
    def __init__(self, readable=True, writable=True, prefix='_', getter=None, setter=None):
        self.readable = readable
        self.writable = writable
        self.prefix = prefix
        self.getter = getter
        self.setter = setter

    def __set_name__(self, owner, name):
        self.name = self.prefix + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if not self.readable:
            raise AttributeError('Attribute reading is forbidden')
        if self.getter:
            return self.getter(instance)
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not self.writable:
            raise AttributeError('Attribute writing is forbidden')
        if self.setter:
            self.setter(instance, value)
        else:
            instance.__dict__[self.name] = value


class ValidatedAttr(Attr):
    def __init__(self, validate=None, **kwargs) -> None:
        if validate:
            self._add_validator(validate)
        super().__init__(**kwargs)

    def __set__(self, instance, value):
        self.validate(instance, value)
        super().__set__(instance, value)

    def _add_validator(self, validator, start=False):
        if not hasattr(self, '_validators'):
            self._validators = []
        if start:
            if isinstance(validator, (list, tuple)):
                self._validators[0:0] = validator
            else:
                self._validators.insert(0, validator)
        else:
            if isinstance(validator, (list, tuple)):
                self._validators.extend(validator)
            else:
                self._validators.append(validator)

    def validate(self, instance, value):
        for validate in getattr(self, '_validators', []):
            if not validate(instance, value):
                raise ValueError('Value {} is not valid'.format(value))


class TypedAttr(ValidatedAttr):
    def __init__(self, type, nullable=False, **kwargs) -> None:
        self.type = type
        self.nullable = nullable
        self._add_validator(self.validate_type, start=True)
        super().__init__(**kwargs)

    def validate_type(self, instance, value):
        if self.nullable and value is None:
            return True
        if not isinstance(value, self.type):
            raise TypeError('Value must be a {} instance'.format(self.type))
        return True


class StringAttr(TypedAttr):
    def __init__(self, min_length=None, max_length=None, **kwargs):
        self.min_length = min_length
        self.max_length = max_length
        self._add_validator(self.validate_string_length)
        super().__init__(type=str, **kwargs)

    def validate_string_length(self, instance, value):
        if self.nullable and value is None:
            return True
        length = len(value)
        if self.min_length is not None and length < self.min_length:
            raise ValueError('String length must be >= {}'.format(self.min_length))
        if self.max_length is not None and length > self.max_length:
            raise ValueError('String length must be <= {}'.format(self.max_length))
        return True


class IntegerAttr(TypedAttr):
    def __init__(self, min_value=None, max_value=None, **kwargs):
        self.min_value = min_value
        self.max_value = max_value
        self._add_validator(self.validate_number_range)
        super().__init__(type=int, **kwargs)

    def validate_number_range(self, instance, value):
        if self.nullable and value is None:
            return True
        if self.min_value is not None and value < self.min_value:
            raise ValueError('Value must be >= {}'.format(self.min_value))
        if self.max_value is not None and value > self.max_value:
            raise ValueError('Value must be <= {}'.format(self.max_value))
        return True


class BooleanAttr(TypedAttr):
    def __init__(self, **kwargs):
        super().__init__(type=bool, **kwargs)


class ListAttr(TypedAttr):
    def __init__(self, item_type=None, min_size=None, max_size=None, **kwargs) -> None:
        self.item_type = item_type
        self.min_size = min_size
        self.max_size = max_size
        self._add_validator(self.validate_list_type)
        self._add_validator(self.validate_list_size)
        if not 'type' in kwargs:
            kwargs['type'] = (list, tuple)
        super().__init__(**kwargs)

    def validate_list_type(self, instance, value):
        if self.nullable and value is None:
            return True
        if self.item_type is not None and not all(isinstance(x, self.item_type) for x in value):
            raise TypeError('Items must be {} instances'.format(self.item_type))
        return True

    def validate_list_size(self, instance, value):
        size = len(value)
        if self.min_size is not None and size < self.min_size:
            raise ValueError('List size must be >= {}'.format(self.min_size))
        if self.max_size is not None and size > self.max_size:
            raise ValueError('List size must be <= {}'.format(self.max_size))
        return True


__all__ = ('Attr', 'ValidatedAttr', 'TypedAttr', 'StringAttr', 'IntegerAttr', 'BooleanAttr', 'ListAttr')
