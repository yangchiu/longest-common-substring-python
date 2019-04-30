def longest_common_substring(s1, s2):
    m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
    longest, s1_end, s2_end = 0, 0, 0
    for x in range(1, 1 + len(s1)):
        for y in range(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    s1_end = x
                    s2_end = y
            else:
                m[x][y] = 0
    return s1_end, s2_end, longest, s1[s1_end - longest: s1_end]

def merge_sentence(s1, s2):
    s1_words = s1.split(' ')
    s2_words = s2.split(' ')

    s1_end, s2_end, longest, substring = longest_common_substring(s1_words, s2_words)
    
    if len(substring) != 0:
        head = s1_words[:s1_end - longest]
        tail = s2_words[s2_end:]
        new_sent = head + substring + tail
        return ' '.join(new_sent)
    else:
        return ''
        
if __name__ == '__main__':
    s1 = 'we are interested in evaluating two closely related variants. One is a long short-term memory (LSTM) unit, and the other is a gated recurrent unit (GRU) proposed more recently by Cho et al. [2014].'
    s2 = 'proposed more recently by Cho et al. [2014]. It is well established in the field that the LSTM unit works well on sequence-based tasks with long-term dependencies, but the latter has only recently been introduced and used in the context of machine translation.'
    
    s1_words = s1.split(' ')
    s2_words = s2.split(' ')
    
    # pass the words lists into lcs function,
    # so it would compare 2 sentences word by word instead of character by character.
    s1_end, s2_end, longest, substring = longest_common_substring(s1_words, s2_words)
    print(f'find common substring in s1[{s1_end - longest}:{s1_end}]')
    print(f'find common substring in s2[{s2_end - longest}:{s2_end}]')
    print(f'common substring = {substring}')
    
    # if there is a common part in these 2 sentences,
    # maybe you want to merge them into 1 sentence.
    merged = merge_sentence(s1, s2)
    if len(merged) != 0:
        print(f'merged 2 strings into: {merged}')
    
    
    
    