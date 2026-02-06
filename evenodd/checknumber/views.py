from django.shortcuts import render

def check(request):
    c = ''
    eo_status = '' # Even/Odd status ke liye naya variable
    try:
        if request.method == "POST":
            val1 = request.POST.get("num1")
            val2 = request.POST.get("num2")
            
            n1 = eval(val1) if val1 else 0
            n2 = eval(val2) if val2 else 0
            opr = request.POST.get("opr")

            # Pehle calculation karein
            if opr == "+":
                c = n1 + n2
            elif opr == "-":
                c = n1 - n2
            elif opr == "*":
                c = n1 * n2
            elif opr == "/":
                c = n1 / n2
            
            # Ab check karein ke result (c) even hai ya odd
            if isinstance(c, (int, float)): # Check ke result number hi hai
                if c % 2 == 0:
                    eo_status = "(Even Number)"
                else:
                    eo_status = "(Odd Number)"
                    
    except Exception as e:
        c = "Invalid Operator...."
    
    # Dono variables 'c' aur 'eo_status' template ko bhej dein
    return render(request, 'evenodd.html', {'c': c, 'eo': eo_status})