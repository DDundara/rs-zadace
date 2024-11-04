def brojanje_riječi(tekst):
    riječi = tekst.split()
    brojač = {}
    for riječ in riječi:
        if riječ in brojač:
            brojač[riječ] += 1
        else:
            brojač[riječ] = 1
    return brojač
tekst = "Python je omiljen među početnicima jer je jednostavan za učenje, a vrlo moćan za profesionalni razvoj."
print(brojanje_riječi(tekst))
