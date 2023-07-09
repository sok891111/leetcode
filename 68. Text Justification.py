class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        tmp = []
        result = []
        count = 0
        cur = []
        for word in words:
            L =len(word) 
            if maxWidth < count + L:
                tmp.append(cur[:])
                count = 0
                cur = []
            cur.append(word)
            count += (L +1 )
        tmp.append(cur)

        for inx in range(len(tmp)-1):
            line = tmp[inx]
            evenly = True
            space = (maxWidth - len(''.join(line)) ) /  max(len(line) -1 , 1)

            cur_line = (' '*space).join(line)
            if maxWidth > len(cur_line) :
                left_padding = maxWidth - len(cur_line)
                cur_line = ''
                for index in range(len(line)-1) :
                    cur_line += line[index]
                    if left_padding > index:
                        cur_line += ' ' * (space +1)
                    else:
                        cur_line += ' ' * space 
                cur_line += line[-1] 
                cur_line += ' '* (maxWidth -len(cur_line))

            result.append(cur_line)
            

        last_line = ' '.join(tmp[-1])
        result.append(last_line + (' '* (maxWidth - len(last_line) ) ))
        
        return result
