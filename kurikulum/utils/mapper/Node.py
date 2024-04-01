from kurikulum.enum.prefix import Prefix


class IRI:
    def __init__(self, prefix: Prefix, value):
        self.prefix = prefix
        self.value = value

    def __str__(self) -> str:
        if self.prefix == Prefix.STRING:
            return f'"{self.value}"^^{self.prefix.value}'
        return f'{self.prefix.value}:{self.value}'