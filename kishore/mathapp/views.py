from django.shortcuts import render

def power(request):
    context = {'power': "0", 'i': "0", 'r': "0"}  # default values

    if request.method == 'POST':
        try:
            # Must match input names from your HTML form (Intensity, Resistance)
            i = float(request.POST.get('Intensity', '0'))
            r = float(request.POST.get('Resistance', '0'))

            # Formula: P = I² * R
            p = (i ** 2) * r

            # Store in context for template
            context['power'] = p
            context['i'] = i
            context['r'] = r

            print("POST method is used")
            print("Intensity =", i)
            print("Resistance =", r)
            print("Power =", p)

        except ValueError:
            context['power'] = "Invalid input"

    return render(request, 'mathapp/math.html', context)
