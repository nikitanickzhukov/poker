from collections import Iterable


def isiterable(instance):
    return isinstance(instance, Iterable)


class Attr():
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        raise NotImplementedError()


class WritableAttr(Attr):
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class ValidatedAttr(WritableAttr):
    def __init__(self, validate) -> None:
        self.validators = self._join_validators(validate)
        super().__init__()

    def __set__(self, instance, value):
        for validate in self.validators:
            if not validate(value):
                raise ValueError('Value is not valid')
        super().__set__(instance, value)

    def _join_validators(self, vlist, vfunc=None):
        if vlist is None:
            vlist = []
        elif not isiterable(vlist):
            vlist = [vlist]
        else:
            vlist = list(vlist)
        if vfunc is not None:
            vlist[0:0] = [vfunc]
        return vlist


class TypedAttr(ValidatedAttr):
    def __init__(self, type, validate=None) -> None:
        def validate_type(value):
            return isinstance(value, type)
        super().__init__(validate=self._join_validators(validate, validate_type))


class StringAttr(TypedAttr):
    def __init__(self, min_length=None, max_length=None, validate=None):
        def validate_length(value):
            if min_length is not None and len(value) < min_length:
                return False
            if max_length is not None and len(value) > max_length:
                return False
            return True
        super().__init__(type=str, validate=self._join_validators(validate, validate_length))


class IntegerAttr(TypedAttr):
    def __init__(self, min_value=None, max_value=None, validate=None):
        def validate_range(value):
            if min_value is not None and value < min_value:
                return False
            if max_value is not None and value > max_value:
                return False
            return True
        super().__init__(type=int, validate=self._join_validators(validate, validate_range))
