class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0

        while i < len(words):
            j = i
            line_length = 0

            while j < len(words) and line_length + len(words[j]) + (j - i) <= maxWidth:
                line_length += len(words[j])
                j += 1

            num_words = j - i
            total_spaces = maxWidth - line_length

            if j == len(words) or num_words == 1:
                line = ' '.join(words[i:j])
                line += ' ' * (maxWidth - len(line))
            else:
                spaces = total_spaces // (num_words - 1)
                extra = total_spaces % (num_words - 1)

                line = ''
                for k in range(i, j - 1):
                    line += words[k]
                    line += ' ' * (spaces + (1 if k - i < extra else 0))

                line += words[j - 1]

            result.append(line)
            i = j

        return result