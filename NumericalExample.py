#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 16:33:04 2021

@author: Guoxin Sun 

Paper: "Strategic mitigation against wireless attacks onautonomous platoons"

It is a numerical example of the proposed security game based mitigation framework.

Please refer to the paper for detailed explanation (especially Section 3).
"""
import gambit 
import sys
import argparse
class ControllerSwitchingStrategy:
    def __init__(self):
        self.payoffsDefender = []
        self.payoffsAttacker = []
    def getPayoffs(self, a_acc=7, a_cacc=-10, na_acc=-5, na_cacc=10, s_d=3, ns_d=-3, s_nd=-3, ns_nd=3):
        """ 
        To compute payoffs
        """
        self.payoffsDefender.append(a_acc+s_d)
        self.payoffsDefender.append(a_cacc+ns_d)
        self.payoffsDefender.append(a_acc+s_nd)
        self.payoffsDefender.append(a_cacc+ns_nd)
        self.payoffsDefender.append(na_acc+s_d)
        self.payoffsDefender.append(na_cacc+ns_d)
        self.payoffsDefender.append(na_acc+s_nd)
        self.payoffsDefender.append(na_cacc+ns_nd)
        print("Defender's Payoffs are ", self.payoffsDefender)
        self.payoffsAttacker.append(-(a_acc+s_d))
        self.payoffsAttacker.append(-(a_cacc+ns_d))
        self.payoffsAttacker.append(-(a_acc+s_nd))
        self.payoffsAttacker.append(-(a_cacc+ns_nd))
        self.payoffsAttacker.append(-(0+s_d))
        self.payoffsAttacker.append(-(na_cacc+ns_d))
        self.payoffsAttacker.append(-(0+s_nd))
        self.payoffsAttacker.append(-(na_cacc+ns_nd))
        print("Attacker's Payoffs are ", self.payoffsAttacker)
        return self.payoffsDefender, self.payoffsAttacker

    def run(self, P_na_nr = (6, 10), P_na_r = (4, 10), P_a_nr = (1, 100), 
            P_a_r = (99, 100),a_acc=7, a_cacc=-10, na_acc=-5, na_cacc=10,s_d=0, ns_d=-6, s_nd=-6, ns_nd=0):
        g = gambit.Game.new_tree()
        g.title = "Controller Switching Game"
        
        P1 = g.players.add("Attacker")
        P2 = g.players.add("Defender")
        
        # to define state-action pair
        
        move = g.root.append_move(P1, 2)
        move.actions[0].label = "na"
        move.actions[1].label = "a"
        
        c1 = g.root.children[0].append_move(g.players.chance, 2)
        c1.actions[0].label = "nr"
        c1.actions[0].prob = gambit.Rational(P_na_nr[0], P_na_nr[1])
        c1.actions[1].label = "r"
        c1.actions[1].prob = gambit.Rational(P_na_r[0], P_na_r[1])
        
        c2 = g.root.children[1].append_move(g.players.chance, 2)
        c2.actions[0].label = "nr"
        c2.actions[0].prob = gambit.Rational(P_a_nr[0], P_a_nr[1])
        c2.actions[1].label = "r"
        c2.actions[1].prob = gambit.Rational(P_a_r[0], P_a_r[1])
        
        set1 = g.root.children[0].children[0].append_move(P2, 2)
        set1.actions[0].label = "cacc"
        set1.actions[1].label = "acc"
        
        set2 = g.root.children[0].children[1].append_move(P2, 2)
        set2.actions[0].label = "cacc"
        set2.actions[1].label = "acc"
        
        g.root.children[1].children[0].append_move(set1)
        g.root.children[1].children[1].append_move(set2)
        
        #payoffs
        payoffsDefender, payoffsAttacker = self.getPayoffs(a_acc=a_acc, a_cacc=a_cacc, na_acc=na_acc, na_cacc=na_cacc, s_d=s_d, ns_d=ns_d, s_nd=s_nd, ns_nd=ns_nd)
        o1 = g.outcomes.add("")
        o1[0] = payoffsAttacker[7]
        o1[1] = payoffsDefender[7]
        o2 = g.outcomes.add("")
        o2[0] = payoffsAttacker[6]
        o2[1] = payoffsDefender[6]
        o3 = g.outcomes.add("")
        o3[0] = payoffsAttacker[5]
        o3[1] = payoffsDefender[5]
        o4 = g.outcomes.add("")
        o4[0] = payoffsAttacker[4]
        o4[1] = payoffsDefender[4]
        o5 = g.outcomes.add("")
        o5[0] = payoffsAttacker[3]
        o5[1] = payoffsDefender[3]
        o6 = g.outcomes.add("")
        o6[0] = payoffsAttacker[2]
        o6[1] = payoffsDefender[2]
        o7 = g.outcomes.add("")
        o7[0] = payoffsAttacker[1]
        o7[1] = payoffsDefender[1]
        o8 = g.outcomes.add("")
        o8[0] = payoffsAttacker[0]
        o8[1] = payoffsDefender[0]
        
        g.root.children[0].children[0].children[0].outcome = o1
        g.root.children[0].children[0].children[1].outcome = o2
        g.root.children[0].children[1].children[0].outcome = o3
        g.root.children[0].children[1].children[1].outcome = o4
        g.root.children[1].children[0].children[0].outcome = o5
        g.root.children[1].children[0].children[1].outcome = o6
        g.root.children[1].children[1].children[0].outcome = o7
        g.root.children[1].children[1].children[1].outcome = o8
        out = gambit.nash.lcp_solve(g, rational=False)

        return out
    def print_NashEquilibrium(self, out):
        print("Prob. of not attacking - P(na) = {:.4f}".format(out[0][0]))
        print("Prob. of initiating boiling frog attack - P(a) = {:.4f}".format(out[0][1]))
        print("If the detector reports NO attack, P(cacc) = {:.4f}, P(acc) = {:.4f}".format(out[0][2], out[0][3]))
        print("If the detector reports an attack, P(cacc) = {:.4f}, P(acc) = {:.4f}".format(out[0][4], out[0][5]))
        

def readCommand( argv ):
    """
    Processes the command used to run the proposed security game based mitigation framework from the command line.
    """
    usageStr = """
    USAGE:      python NumericalExample.py <options>
    EXAMPLES:   (1) python NumericalExample.py
                    - returns the Player' payoffs, prob. of initiating an attack and prob. of defloying acc for defending 
                (2) python NumericalExample.py -p
                    - starts to type in utility values and detector properties for game tree construction
    """
    parser = argparse.ArgumentParser(usageStr)
      
    parser.add_argument("-p", "--parameters", help="enter utility values and detector properties", action="store_true", default=False)
      
    args = parser.parse_args(argv)
    global alpha_d, alpha_f, alpha_m, beta_s, beta_t, P_na_nr, P_na_r, P_a_nr, P_a_r
    if args.print_string:
        alpha_d = int(input('Enter alpha_d: '))
        alpha_f = int(input('Enter alpha_f: '))
        alpha_m = int(input('Enter alpha_m: '))
        beta_s = int(input('Enter beta_s: '))
        beta_t = int(input('Enter beta_t: '))
        false_alarm = int(100*round(float(input('Enter Prob. of false alarms:')),2)) # format required by the chance node defination in Gambit
        misses = int(100*round(float(input('Enter Prob. of misses:')),2))
        P_na_nr = (100-false_alarm,100)
        P_na_r = (false_alarm, 100)
        P_a_nr = (misses, 100)
        P_a_r = (100-misses, 100)
    else:
        # Default vaules (same as the ones presented in the paper)
        
        # Entries of utility function U1  
        alpha_d = 5
        alpha_f = 9
        alpha_m = 12
        
        # Entries of utility function U2
        beta_s = 10
        beta_t = 15
        # =============================================================================
        #     # When the defense framework is depolyed on each vehicle, beta_s is caulated as (please refer to eq.(6) in the paper)
        #     if eps_radar > eps_max:
        #         beta_s = int(6*np.log2(10*eps_radar))
        #     else:
        #         beta_s = -k_c
        # =============================================================================
        
        # Detector properties 
        P_na_nr = (85, 100)
        P_na_r = (15, 100)
        P_a_nr = (35, 100)
        P_a_r = (65, 100)

        
    
if __name__ == '__main__':
    options = readCommand( sys.argv[1:] )

    NumericalExample= ControllerSwitchingStrategy()
    Results = NumericalExample.run(P_na_nr = P_na_nr, P_na_r = P_na_r, P_a_nr = P_a_nr, P_a_r = P_a_r,
                                        a_acc=alpha_d, a_cacc=-alpha_m, na_acc=-alpha_f, na_cacc=0,
            s_d=beta_t, ns_d=beta_s, s_nd=beta_s, ns_nd=beta_t)
    NumericalExample.print_NashEquilibrium(Results)       