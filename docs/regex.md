## regular expression

#### search(pattern, string, flags=0)
Tìm kiếm vị trí đầu tiên mà chuỗi regex trùng khớp chuỗi cần so.
- pattern: chuỗi regex
- string: chuỗi cần so
- flag: *bên dưới

Trả về một `Match object` nếu không trùng trả về `None`
```
_str = 'abababababab'
re.search(r'a', _str)
______________________Output___________________
<_sre.SRE_Match object; span=(0, 1), match='a'>
```

#### match(pattern, string, flags=0)
So vị trí đầu tiên của chuỗi cần so với chuỗi regex
- pattern: chuỗi regex
- string: chuỗi cần so
- flag: *bên dưới

Trả về một `Match object` nếu không trùng trả về `None`
```
_str = 'abababababab'
re.match(r'a', _str)
______________________Output___________________
<_sre.SRE_Match object; span=(0, 1), match='a'>
```

#### fullmatch(pattern, string, flags=0)
So cả chuỗi có trùng với chuỗi regex
- pattern: chuỗi regex
- string: chuỗi cần so
- flag: *bên dưới

Trả về một `Match object` nếu không trùng trả về `None`
```
_str = 'abababababab'
re.search(r'abababababab', _str)
______________________Output___________________
<_sre.SRE_Match object; span=(0, 1), match='a'>
```

#### split(pattern, string, maxsplit)
Cắt chuỗi cần so tại vị trí trùng với chuỗi regex
- pattern: chuỗi regex
- string: chuỗi cần so
- maxsplit: số lần cắt tối đa
 
Trả về một `list` các `str` sau khi cắt
```
_str = 'abababababab'
re.split(r'a', _str)
_______________Output_____________
['', 'b', 'b', 'b', 'b', 'b', 'b']
```

#### sub(pattern, repl, string, count=0, flags=0)
Thay thế tất cả các chuỗi trong `string` phù hợp với chuỗi `pattern`
- pattern: chuỗi regex
- repl: chuỗi thay thế
- string: chuỗi cần so
- count: số chuỗi thay thế
- flag: *bên dưới
 
Trả về một `str` sau khi thay thế 
```
_str = 'abababababab'
re.sub(r'a','c',_str, 2)
_______________Output_____________
'cbcbabababab'
```

#### subn(pattern, repl, string, count=0, flags=0)
Giống sub() nhưng trả về 1 `tuple`: (chuỗi mới, số lần thay thế)
```
_str = 'abababababab'
re.subn(r'a','c',_str, 2)
_______________Output_____________
('cbcbabababab', 2)
```

#### escape(pattern)

#### purge()
xóa regex cache

#### re.compile(pattern, flags=0)

#### flag
|flag|description|
|----|-----------|
|`re.A`  or `re.ASCII`|chỉ ký tự ASCII|
|`re.DEBUG`||
|`re.I` or `re.IGNORECASE`|không phân biệt hoa thường|
|`re.L` or `re.LOCALE`||
|`re.M` or `re.MULTILINE`||
|`re.S` or `re.DOTALL`|`.` trùng với tất cả các ký tự kể cả `newline`|
|`re.X` or `re.VERBOSE`|cho phép bỏ qua `space` và comment trong regex|

### regex
`.` trùng với bất kỳ ký tự nào trừ `newline`, nếu có cờ `re.S` thì trùng với tất cả
```
st = 'aba aca a\na'
re.findall(r'a.a', st)
________Output________
['aba', 'aca']

re.findall(r'a.a', st, re.S)
________Output________
['aba', 'aca', 'a\na']
```

`^` Matches the start of the string, and in `re.M` mode also matches immediately after each newline.
```
st = "abc\nacd\nade\n"
re.findall(r'^a.', st)
________Output________
['ab']

re.findall(r'^a.', st, re.M)
________Output________
['ab', 'ac', 'ad']
```

`$` Matches the end of the string or just before the newline at the end of the string, and in `re.M` mode also matches before a newline. 
```
st = "abc\nbcc\ndec"
re.findall(r'..c$', st)
________Output________
['dec']

re.findall(r'..c$', st, re.M)
________Output________
['abc', 'bcc', 'dec']
```

`*` trùng với 0 hay nhiều ký tự đứng trước
```
st = 'aa ab abb'
re.findall(r'ab*', st)
________Output________
['a', 'a', 'ab', 'abb']

```

`+` trùng với 1 hay nhiều ký tự đứng trước
```
st = 'ab aab aaab'
re.findall(r'a+', st)
________Output________
['a', 'aa', 'aaa']

re.findall(r'aa+', st)
________Output________
['aa', 'aaa']
```

`?` trùng với 0 hay 1 ký tự đứng trước
```
st = 'ab ac ad'
re.findall(r'ab?', st)
________Output________
['ab', 'a', 'a']
```

`{m}` Specifies that exactly m copies of the previous RE should be matched; fewer matches cause the entire RE not to match. For example, `a{6}` will match exactly six `a` characters, but not five.
```
st = 'a aa aaa aaaa aaaaa'
re.findall(r'a{3}', st)
__________Output__________
['aaa', 'aaa', 'aaa']
```

`{m,n}` Causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as many repetitions as possible. For example, `a{3,5}` will match from 3 to 5 'a' characters. Omitting m specifies a lower bound of zero, and omitting n specifies an infinite upper bound. As an example, `a{4,}b` will match 'aaaab' or a thousand 'a' characters followed by a 'b', but not 'aaab'. The comma may not be omitted or the modifier would be confused with the previously described form.
```
st = 'ab aab aaab aaaab aaaaab'
re.findall(r'a{2,3}b', st)
____________Output_____________
['aab', 'aaab', 'aaab', 'aaab']
```

`{m,n}?` Causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as few repetitions as possible. This is the non-greedy version of the previous qualifier. For example, on the 6-character string 'aaaaaa', `a{3,5}` will match 5 'a' characters, while `a{3,5}?` will only match 3
characters.
```
st = 'ab aab aaab aaaab aaaaab'
re.findall(r'a{2,3}?', st)
____________Output_____________
['aa', 'aa', 'aa', 'aa', 'aa', 'aa']

re.findall(r'a{2,3}', st)
____________Output_____________
['aa', 'aaa', 'aaa', 'aaa', 'aa']
```

`[]` Used to indicate a set of characters. In a set:
- Characters can be listed individually, e.g. [amk] will match 'a', 'm', or 'k'.
```
st = 'aa ab ac ad ae'
re.findall(r'a[bcd]', st)
____________Output_____________
['ab', 'ac', 'ad']
```
- Ranges of characters can be indicated by giving two characters and separating them by a '-', for example [a-z] will match any lowercase ASCII letter, [0-5][0-9] will match all the two-digits numbers from 00 to 59, and [0-9A-Fa-f] will match any hexadecimal digit. If - is escaped (e.g. [a\-z]) or if it’s placed as the first or last character (e.g. [-a] or [a-]), it will match a literal '-'.
```
st = 'aa ab ac ad ae af ag'
re.findall(r'a[b-f]', st)
____________Output_____________
['ab', 'ac', 'ad', 'ae', 'af']

st = 'a- -a --a a--'
re.findall(r'a[-]', st)
____________Output_____________
['a-', 'a-']

re.findall(r'a[\-]', st)
____________Output_____________
['a-', 'a-']
```
- Special characters lose their special meaning inside sets. For example, [(+*)] will match any of the literal characters '(', '+', '*', or ')'.
- Character classes such as \w or \S (defined below) are also accepted inside a set, although the characters they match depends on whether ASCII or LOCALE mode is in force.
- Characters that are not within a range can be matched by complementing the set. If the first character of the set is '^', all the characters that are not in the set will be matched. For example, [^5] will match any character except '5', and [^^] will match any character except '^'. ^ has no special meaning if it’s not the first character in the set.
```
st = 'aa ab ac ad ae'
re.findall(r'a[^bcs]', st)
____________Output__________
['aa', 'ad', 'ae']
```
- To match a literal ']' inside a set, precede it with a backslash, or place it at the beginning of the set. For example, both [()[\]{}] and []()[{}] will both match a parenthesis.
- Support of nested sets and set operations as in Unicode Technical Standard #18 might be added in the future. This would change the syntax, so to facilitate this change a FutureWarning will be raised in ambiguous cases for the time being. That includes sets starting with a literal '[' or containing literal character sequences '--', '&&', '~~', and '||'. To avoid a warning escape them with a backslash.

`|` Example `A|B`, where A and B can be arbitrary REs, creates a regular expression that will match either A or B. An arbitrary number of REs can be separated by the '|' in this way. This can be used inside groups (see below) as well. As the target string is scanned, REs separated by '|' are tried from left to right. When one pattern completely matches, that branch is accepted. This means that once A matches, B will not be tested further, even if it would produce a longer overall match. In other words, the '|' operator is never greedy. To match a literal '|', use \|, or enclose it inside a character class, as in [|].
```
st = 'aa ab bb'
re.findall(r'aa|bb', st)
____________Output__________
['aa', 'bb']

re.findall(r'aa|bb|ab', st)
____________Output__________
['aa', 'ab', 'bb']
```

`(...)` Matches whatever regular expression is inside the parentheses, and indicates the start and end of a group; the contents of a group can be retrieved after a match has been performed, and can be matched later in the string with the `\number` special sequence, described below. To match the literals '(' or ')', use `\(` or `\)`, or enclose them inside a character class: `[(]`, `[)]`.
```
st = 'aac acc aacc acac caca ccaa'
re.findall(r'(ac)', st)
____________Output__________
['ac', 'ac', 'ac', 'ac', 'ac']
```

`(?imx)` Temporarily toggles on i, m, or x options within a regular expression. If in parentheses, only that area is affected.

`(?-imx)` Temporarily toggles off i, m, or x options within a regular expression. If in parentheses, only that area is affected.

`(?: re)` Groups regular expressions without remembering matched text.

`(?imx: re)` Temporarily toggles on i, m, or x options within parentheses.

`(?-imx: re)` Temporarily toggles off i, m, or x options within parentheses.

`(?#...)` Comment.

`(?= re)` Specifies position using a pattern. Doesn't have a range.

`(?! re)` Specifies position using pattern negation. Doesn't have a range.

`(?> re)` Matches independent pattern without backtracking.

`\w` Matches word characters.

`\W` Matches nonword characters.

`\s` Matches whitespace. Equivalent to [\t\n\r\f].

`\S` Matches nonwhitespace.

`\d` atches digits. Equivalent to [0-9].

`\D` Matches nondigits.

`\A` Matches beginning of string.

`\Z` Matches end of string. If a newline exists, it matches just before newline.

`\z` Matches end of string.

`\G` Matches point where last match finished.

`\b` Matches word boundaries when outside brackets. Matches backspace (0x08) when inside brackets.

`\B` Matches nonword boundaries.

`\n, \t, etc.` Matches newlines, carriage returns, tabs, etc.

`\1...\9` Matches nth grouped subexpression.

`\10` Matches nth grouped subexpression if it matched already. Otherwise refers to the octal representation of a character code.
