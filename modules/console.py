"""
Console module for the calculator.
"""
from modules.commands import Commands
from modules.board import Board
from modules.tools import pretty
import re

class Console:
    def __init__(self,cmds,brd,prt=print,inp=input) -> None:
        self.cmds = cmds
        self.prt = prt
        self.inp = inp
        self.running = False
    
    def run(self):
        self.prt("SYMCALC v1.0")
        self.running = True
        while self.running:
            cmd = self.inp(">>> ").strip()
            if cmd:
                try:
                    res = self.parse(cmd)
                    if res[0] == 0:
                        retour = pretty(res[1])
                        self.running = False
                    elif res[0] in (0,"$"):
                        retour = pretty(res[1])
                    else:
                        retour = pretty(res[1],ante=res[0]+" = ")
                    self.prt(retour)
                except Exception as e:
                    self.prt("Error: "+str(e))

    def parse(self,cmd):
        cmd_split = re.split(r"\s+",cmd)
        if cmd_split[0][0] == "!":
            if cmd_split[0][1:] in dir(self.cmds):
                return getattr(self.cmds,cmd_split[0][1:])(*cmd_split[1:])
            else:
                return None,"Invalid command."
        elif cmd_split[0][0] == "+":
            return self.cmds.add(cmd_split[0][1:] + " ".join(cmd_split[1:]))
        elif cmd_split[0][0] == "-":
            return self.cmds.sub(cmd_split[0][1:] + " ".join(cmd_split[1:]))
        elif cmd_split[0][0] == "*":
            return self.cmds.mul(cmd_split[0][1:] + " ".join(cmd_split[1:]))
        elif cmd_split[0][0] == "/":
            return self.cmds.div(cmd_split[0][1:] + " ".join(cmd_split[1:]))
        else:

            match = re.match(r"^([\S\s]+)={2}([\S\s]+)$",cmd)
            if match:
                return self.cmds.solve(match.group(1).strip(),match.group(2).strip())
            match = re.match(r"^([\S\s]+)=([\S\s]+)$",cmd)
            if match:
                return self.cmds.set(match.group(1).strip(),match.group(2).strip())
            match = re.match(r"^([\S\s]+):([\S\s]+)$",cmd)
            if match:
                return self.cmds.func(match.group(1).strip(),match.group(2).strip())
            
            return self.cmds.set("$",cmd)
        
        

brd = Board()
cmds = Commands(brd)
console = Console(cmds,brd)