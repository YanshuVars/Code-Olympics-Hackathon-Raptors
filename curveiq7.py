# CurveIQ — Compact Curve Analyzer (≤200 lines)

from sympy import *
import numpy as np, matplotlib.pyplot as plt
x = symbols('x')

# ---------- Utility ----------
def sf(f,*a):
    try: return f(*a)
    except Exception as e: return f"ERR:{e}"

def pin(s): 
    try: return sympify(s)
    except: raise ValueError("Bad expr")

def fmt(e):
    s = str(e)
    return (s.replace("**","^")
             .replace("*x","x")
             .replace("*(","(")
             .replace("I","i"))

def gtp(e):
    s = str(e)
    if any(k in s for k in ("sin","cos","tan")): return "trig"
    if "exp(" in s or "E**" in s: return "exp"
    if "log(" in s: return "log"
    return "gen"

def dfx(e): return sf(diff,e,x)
def itg(e): return sf(integrate,e,x)
def rts(e): return sf(lambda: solve(e,x))

def limv(e,p):
    try: return limit(e,x,p,'-'), limit(e,x,p,'+')
    except Exception as ex: return f"ERR:{ex}", f"ERR:{ex}"

def cnt(e,p):
    try:
        l,r=limv(e,p)
        if isinstance(l,str) or isinstance(r,str): return 0
        v=e.subs(x,p); return l==r==v
    except: return 0

def per(e):
    s=str(e)
    if "sin" in s or "cos" in s: return "2π"
    if "tan" in s: return "π"
    return "Non-periodic"

# ---------- Plotting ----------
def pltf(fx,gx=None,a=-10,b=10,n=400):
    try:
        f=lambdify(x,fx,'numpy'); xs=np.linspace(a,b,n); ys=f(xs)
        plt.figure(figsize=(6,3)); plt.plot(xs,ys,label="f(x)")
        if gx is not None:
            g=lambdify(x,gx,'numpy'); yg=g(xs)
            plt.plot(xs,yg,label="g(x)")
            its=sf(lambda: solve(fx-gx,x)); pts=[]
            for xi in its:
                try:xv=float(xi); yv=float(fx.subs(x,xv)); pts.append((round(xv,3),round(yv,3)))
                except: pass
            if pts:
                X,Y=zip(*pts); plt.scatter(X,Y,c='r',label='int'); print("Intersections:",fmt(pts))
            else: print("No intersection.")
        plt.axhline(0,c='k',lw=0.5); plt.grid(1); plt.legend()
        plt.title(fmt(fx)); plt.show()
    except Exception as e: print("Plot err:",e)

# ---------- Analysis ----------
def anl(fx):
    o=[f"Expr: {fmt(fx)}",
       "Type: "+gtp(fx),
       "Diff: "+fmt(dfx(fx)),
       "Intg: "+fmt(itg(fx)),
       "Root: "+fmt(rts(fx)),
       "Per: "+fmt(per(fx))]
    return "\n".join(o)

def dbg(fx):
    print(f"\n🔍 Curve Debug for: {fmt(fx)}")
    try:
        d1,d2=diff(fx,x),diff(fx,x,2); num,den=fx.as_numer_denom()
        bad=[p for p in solve(den,x) if p.is_real]
        print("Domain excludes:",[fmt(p) for p in bad] if bad else "None")
        for p in bad:
            L,R=limit(fx,x,p,'-'),limit(fx,x,p,'+')
            if any(abs(v)==np.inf for v in [L,R]): print(f"Vert asymptote x={fmt(p)}")

        try: crt=sorted([c for c in solve(d1,x) if c.is_real])
        except:
            crt=[]; fnum=lambdify(x,d1,'numpy'); xs=np.linspace(-20,20,800)
            for i in range(len(xs)-1):
                try:
                    if fnum(xs[i])*fnum(xs[i+1])<0: crt.append((xs[i]+xs[i+1])/2)
                except: pass
        crt=sorted(set([round(float(c),3) for c in crt if abs(c)<1e4]))
        if not crt: print("No stationary pts — monotonic.")
        inc,dec=[],[]; pts=[-np.inf]+crt+[np.inf]
        for i in range(len(pts)-1):
            mid=(pts[i]+pts[i+1])/2 if np.isfinite(pts[i]) and np.isfinite(pts[i+1]) else 0
            try:v=float(d1.subs(x,mid))
            except: continue
            seg=f"({fmt(pts[i])},{fmt(pts[i+1])})"; (inc if v>0 else dec).append(seg)
        for c in crt:
            try:
                y=float(fx.subs(x,c)); s1,s2=float(d1.subs(x,c-0.1)),float(d1.subs(x,c+0.1))
                n="max" if s1>0 and s2<0 else "min" if s1<0 and s2>0 else "flat"
                print(f"x={c}, y={round(y,3)} → {n}")
            except: pass
        if inc: print("Inc:",inc)
        if dec: print("Dec:",dec)
        inf=[p for p in solve(d2,x) if p.is_real]
        if inf: print("Infl pts:",[fmt(p) for p in inf])
        l,r=limit(fx,x,-oo),limit(fx,x,oo)
        if l.is_real and r.is_real: print(f"Horz asymptote: y→{fmt(l)}(L), {fmt(r)}(R)")
        if fx.subs(x,-x)==fx: print("Sym: Even (y-axis)")
        elif fx.subs(x,-x)==-fx: print("Sym: Odd (origin)")
        else: print("Sym: None")
    except Exception as e: print("Dbg err:",e)

# ---------- CLI ----------
def hlp():
    return """Cmds:
 expr <f>  set expr
 dbg       curve debugger
 diff      derivative
 int       integral
 roots     roots
 lim p     L/R limits
 cont p    continuity
 per       period
 plot [a b] plot
 inter [f] intersection
 quit      exit
"""

def main():
    print("CurveIQ — Mini Analyzer"); fx=None
    while 1:
        try: cmd=input(">> ").strip()
        except (EOFError,KeyboardInterrupt): print("\nBye"); return
        if not cmd: continue
        tk=cmd.split(); c=tk[0].lower()
        if c in("q","quit","exit"): print("Bye"); return
        if c in("h","help"): print(hlp()); continue
        if c=="expr" and len(tk)>=2:
            s=cmd[len("expr "):]
            try: fx=pin(s); print(anl(fx))
            except Exception as e: print("Bad expr:",e)
            continue
        if fx is None: print("No expr set."); continue
        if c=="diff": print(fmt(dfx(fx)))
        elif c=="int": print(fmt(itg(fx)))
        elif c=="roots": print(fmt(rts(fx)))
        elif c=="lim" and len(tk)>=2:
            try:p=sympify(tk[1]); l,r=limv(fx,p); print("LHL:",fmt(l),"RHL:",fmt(r))
            except: print("Bad point")
        elif c=="cont" and len(tk)>=2:
            try:p=sympify(tk[1]); print("Cont at",fmt(p),"?",cnt(fx,p))
            except: print("Bad point")
        elif c=="per": print("Per:",fmt(per(fx)))
        elif c=="plot":
            a,b=-10,10
            if len(tk)>=3:
                try:a=float(tk[1]); b=float(tk[2])
                except: print("Bad bounds"); continue
            pltf(fx,a=a,b=b)
        elif c=="inter":
            if len(tk)>=2:
                s2=cmd[len("inter "):]
                try:g=pin(s2)
                except: print("Bad expr"); continue
                pltf(fx,g)
            else: pltf(fx,0)
        elif c=="dbg": dbg(fx)
        else: print("Unknown cmd. Type 'help'.")
        print("-"*40)

if __name__=="__main__": main()
