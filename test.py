#!/usr/bin/env python3
import math
import random
import sys


question_ = r"""
    A farmer sells his product at a loss of %s\%%. If his S.P. was Rs %s, what was his actual loss? What was his cost price?
"""
answer_ = r"""
    Let the C.P be $x$\\
    We have, S.P. = Rs %s,Loss $= %s\%%$\\
    Loss $= \frac{%s}{100}\times x=\frac{%sx}{%s}$\\
    S.P. = C.P. - Loss\\
    \[%s = x - \frac{%sx}{%s}\]
    \[%s =\frac{%sx}{%s}\]
    \[x =Rs%s\]
    Loss $=%s - %s = Rs %s$\\
"""

Steps = [
  {
    "step": r"""
          $$ \text{ Let the C.P be }  x  $$
          $$ \text { We have, S.P. = Rs } %s,
             \text{ Loss } = %s $$
          """,
    "verifier": "",
    "explain": r""" $$ \text{ Please refer back to  the question. The sales price is
           mentioned as Rs %s and loss percentage as %s percent.  } $$
          """
  },
  {
    "step":  r"""
          $$ \text{ Loss = } \frac{%s}{100}\times
             x=\frac{%sx}{%s} $$
              """,
    "verifier": "",
    "explain": r""" $$ \text {%s percent means } \frac{%s}{100}
             \text{ which becomes } \frac{%s}{%s} \text { after simplification.}  $$
           """
  }]


loss_per = 15
sp = 20000
cp = (sp*100) // (100-loss_per)
h = 5

question = question_ % (loss_per, sp)
answer = answer_ % (sp, loss_per, loss_per, loss_per // h, 100 // h,
                            sp, loss_per // h, 100 // h,
                            sp, 100 // h - loss_per // h, 100 // h, cp,
                            cp, sp, cp - sp)

step_args = [[sp, loss_per],
             [loss_per, loss_per // h, 100 // h]]

explainer_args = [[sp, loss_per],
                  [loss_per, loss_per, loss_per // h, 100 // h]]
step_args.extend([[sp,loss_per // h, 100 // h],[cp],[cp,sp,cp-sp]])
explainer_args.extend([[sp,loss_per // h, 100 // h,sp, 100 // h - loss_per // h, 100 // h],[100 // h - loss_per // h,sp,100 // h,sp*(100 // h),100 // h - loss_per // h,cp],[cp,sp,cp-sp]])
Steps.extend([{
    "step":  r"""
          $$ \text{ S.P. = C.P. - Loss } $$
          $$ \text{ S.P. = Rs } %s \text{ and Loss =} frac{%sx}{%s} $$
              """,
    "verifier": "",
    "explain": r""" $$ \text{ Substituting the values of S.P. and Loss, we get} $$
             $$ %s = x - \frac{%sx}{%s} $$
             $$ \text{which simplifies to} $$
             $$ %s = \frac{%sx}{%s} $$
           """
  },
  {
    "step":  r"""
          $$ \text{ Solving for x gives} $$
          $$ x =Rs%s $$
              """,
    "verifier": "",
    "explain": r""" $$ \text{By cross multiplying the equation in the previous step, we get} $$
             $$ %sx = %s \times %s $$
             $$ x = \frac{%s}{%s} $$
             $$ \text{which simplifies to} $$
             $$ x =Rs%s $$
           """
  },
  {
    "step":  r"""
          $$ \text{ Loss = } %s - %s = Rs %s $$
              """,
    "verifier": "",
    "explain": r""" $$ \text{Substituting the value of x in the equation Loss = S.P. - C.P., we get} $$
             $$ \text{Loss = Rs } %s - Rs %s = Rs %s $$
           """
  }
  ])


print(question)
print(answer)



for i,s in enumerate(Steps):
  txt = s["step"] % (tuple(step_args[i]))
  print("Step  %s: %s" % (i+1, txt))
  txt = s["explain"] % (tuple(explainer_args[i]))
  print("Explanation of step %s: %s" % (i+1, txt))

  