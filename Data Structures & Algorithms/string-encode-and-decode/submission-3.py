class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for s in strs:
            encoded_string += f'{len(s)}#{s}'
        
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strings, i = [], 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i : j])

            string = s[j + 1 : j + 1 + length]
            decoded_strings.append(string)

            i = j + 1 + length
        
        return decoded_strings