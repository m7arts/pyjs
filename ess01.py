class SpecialNonValue :
    __slots__ = []
    def __nonzero__() : return False
V_UNDEFINED = SpecialNonValue()
V_EMPTY = SpecialNonValue()

