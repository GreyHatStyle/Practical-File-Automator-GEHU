# test file should start with "test_{anything}.py"

from Language_Selection.Cpp import * 


def test_bracket_conent():
    inp = "cin>>a>>BBBC>>hgighthgh;"
    exp_op = "cout<<a<<BBBC<<hgighthgh<<endl;"
    
    ans = CPP_Complier.bracket_content(CPP_Complier, s=inp)
    print(ans)
    assert ans == exp_op
