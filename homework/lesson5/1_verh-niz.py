def niznij_registr(n):
  return n.lower()
def verh_registr(n):
  return n.upper()
print(niznij_registr('I liKe PyThon'))
print(verh_registr('I liKe PyThon'))
a="My TeacHer is SUper".split()
print(list(map(niznij_registr,a)))
print(list(map(verh_registr,a)))

def is_prime(t):
    if t in (1,2,3):
        return True
