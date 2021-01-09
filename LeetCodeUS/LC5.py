def LC5(s):
    def dfs_single(i,l):
        nonlocal  res
        if i+l >= m or i-l < 0:
            return
        elif s[i+l] == s[i-l]:
            if len(res)< 2*l+1:
                res = s[i-l:i+l+1]
            dfs_single(i,l+1)

    def dfs_due(i,l):
        nonlocal res
        if i + l+1 >= m or i - l < 0:
            return
        elif s[i + l+1] == s[i - l]:
            if len(res) < 2 * l + 2:
                res = s[i - l:i + l + 2]
            dfs_due(i, l + 1)
        return
    m  = len(s)
    res = ''
    for i in range(m):
        dfs_single(i,1)
        if i +1 < m and s[i] == s[i+1]:
            dfs_due(i,0)
    return res
print(LC5("xfsxwjqovpvchyjzdqphjsligzljscmzmjzelmbfnqpukbninfbbljouesngmbdyzhqysroeyagglkgorllkrcditzisqhihmithgjcpilkgfdxxqqjpqnoavgkjhojrldsyucfgtzimdbjehrxxqlpaqdddzismsodvternodzxusuehllpujmjjukrilrubbwzdjxbpmvmmwzbrxcxsjsqljjezgyzmsjpucghjxksdfyucpbvwloyhwevzgudhpspgtvsbjqlzmpequxthdonvbmjpeirttllvmtonqmbqxqtdkgichbfzkbhmhotqpkaeshhecshqjvdwgwkegmujwcnmseicesxddrvutxomsgjeylpqiuyezdccarsiprmoqgyifidxhufocfdrbnqczhtztutspaftwctsmynozhakqgvfsvoffyslhoaptkcktopabrxxwrcbyfftleaotwpoqvjjdzxwwqxjnyszjqwjsghkzpvirwnwgsofkjluyxzgboxybzhnmqhkwgltwdjgnemaaadvflrzdqmjufwyuwzoimnvhlxhxjywbopresdrepulsaaexdeddyzeosqfwlnovfpxothrcxhxnumnymofkkuxvclwvuhcelieengfbhvinckrpbjuuewnwvnrvimgmpsfdlcffpdfwmydgzdvluaejwalueygvvojfovuxwhlwojldfpieqqpoqfxhbkcnrtzrnbaagonnawwaqdzamhnvwdtoxlkexihvrqwwimjn"
))
print(LC5("babad"))
print(LC5("baabad"))
print(LC5("cbbd"))
print(LC5("c"))
