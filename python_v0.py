zero  = lambda _, x: x
one   = lambda f, x: f(x)
two   = lambda f, x: f(f(x))
three = lambda f, x: f(f(f(x)))
four =  lambda f, x: f(f(f(f(x))))
five =  lambda f, x: f(f(f(f(f(x)))))

to_python_int = lambda n: n(lambda x: x + 1, 0)

true =  lambda t, _: t
false = lambda _, f: f

pred_nested = lambda x, next: lambda _: lambda c: c(x, next)

pred_step = lambda f: (lambda g: g(g))(lambda s: lambda acc: lambda c: c(f(acc), lambda _: s(s)(f(acc)) ))

pred = lambda num: lambda f, x: num(lambda v: v(x)(false), pred_nested(x, pred_nested(x,  pred_step(f))) )(x)(true)

sub = lambda first, second: lambda f, x: first(lambda v: v(x)(false), second(lambda next: pred_nested(x, next), pred_nested(x, pred_step(f))) )(x)(true)

assert(to_python_int(pred(zero)) == 0)
assert(to_python_int(pred(one)) == 0)
assert(to_python_int(pred(two)) == 1)
assert(to_python_int(pred(three)) == 2)
assert(to_python_int(pred(five)) == 4)
assert(to_python_int(sub(four, three)) == 1)
assert(to_python_int(sub(three, one)) == 2)
assert(to_python_int(sub(three, two)) == 1)
assert(to_python_int(sub(one, three)) == 0)
assert(to_python_int(sub(one, five)) == 0)
