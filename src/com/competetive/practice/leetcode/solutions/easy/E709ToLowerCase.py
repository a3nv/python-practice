class E709ToLowerCase:
    def to_lower_case(self, value: str) -> str:

        def is_upper(x): return 'A' <= x <= 'z'

        def to_lower(x): return chr(ord(x) | 32)

        return ''.join(to_lower(x) if is_upper(x) else x for x in value)
