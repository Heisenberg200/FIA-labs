from production import IF, AND, THEN, OR, DELETE, NOT, FAIL, backward_chain, forward_chain
# TODO: implement your own rules according to the defined goal tree
# HINT: see an example in the file rules_example_zookeeper.py

class K_classStars:
     has_tenbillion_lifecycle = "(?x) does it have a 10 billion year lifecycle?"
     has_yellow_spectre_light= "(?x) it has the yellow spectral light"
     conclusion = "(?x) Is a K_class star"
     def questions(self):     
        return [self.has_tenbillion_lifecycle, self.has_yellow_spectre_light]
class O_classStars:
     has_million_lifecycle = "(?x) does it have a few million lifecycle"
     has_huge_mass = "(?x) does it have a huge mass"
     has_a_blue_spectre = "(?x) does it have a blue light spectre?"
     conclusion = "(?x) is a O-Class Star"
     def questions(self):     
        return [self.has_million_lifecycle, self.has_a_blue_spectre, self.has_huge_mass]
class M_classStar:
    has_hundred_billion_lifecycle = "(?x) does it have a hundred billion lifecycle?"
    has_a_red_light_spectre = "(?x) does it have a red light spectre"
    has_low_mass = "(?x) does it have a low mass"
    conclusion = "(?x) it is a M-class star"
    def questions(self):
        return(self.has_hundred_billion_lifecycle, self.has_a_red_light_spectre, self.has_low_mass)
class B_classStar:
     has_ten_million_lyfecicle = "(?x) does it a ten million life cycle"
     has_a_very_big_mass = "(?x) does it have a very big mass"
     has_a_blue_white_light_spectre = "(?x) does it have a blue-white light spectre"
     conclusion = "(?x) is a B class star"
     def questions(self):
         return(self.has_a_very_big_mass, self.has_ten_million_lyfecicle, self.has_a_blue_white_light_spectre)
class A_classStar:
    has_hundred_million_lyfecycle = "(?x) does it have a hundred million lifecycle"
    has_impressive_mass = "(?x) does it have an impressive mass"
    has_white_light_spectre = "(?x) does it have a white light specre"
    conclusion = "(?x) it is a A-class Star"
    def questions(self):
        return(self.has_hundred_million_lyfecycle, self.has_impressive_mass, self.has_white_light_spectre) 
class F_class_Star:
    has_15_billion_lifecycle = "(?x does it have a 15 billion lifecycle)"
    has_sun_mass = "(?x) does it have the sun mass"
    has_orrange_light_spectre = "(?x) does it have orange light spectre"
    conclusion = "(?x) it is a orange F-class star"
    def questions(self):
        return(self.has_15_billion_lifecycle, self.has_sun_mass, self.has_orrange_light_spectre)
StarClass_RuleSet = (
    #stars that will live for a very long time
    IF(AND(K_classStars.has_tenbillion_lifecycle),
     THEN(K_classStars.conclusion)),
     #stars that will have a short lifecycle 
    IF(AND(O_classStars.has_a_blue_spectre, O_classStars.has_million_lifecycle),
       THEN(O_classStars.conclusion)),
    IF(AND(B_classStar.has_a_blue_white_light_spectre, B_classStar.has_a_very_big_mass),
       THEN(B_classStar.conclusion)),
    IF(AND(A_classStar.has_white_light_spectre, A_classStar.has_hundred_million_lyfecycle), 
       THEN(A_classStar.conclusion)),
    IF(AND(M_classStar.has_a_red_light_spectre, M_classStar.has_hundred_billion_lifecycle),
       THEN(M_classStar.conclusion)),
    #stars that will end up in white dwarfs
    ##IF(AND(K_classStars.has_tenbillion_lifecycle, K_classStars.has_yellow_spectre_light),
       ##THEN(K_classStars.conclusion)),
    IF(AND(F_class_Star.has_orrange_light_spectre, F_class_Star.has_15_billion_lifecycle, F_class_Star.has_sun_mass),
       THEN(F_class_Star.conclusion)),
    #stars that will wnd up in neutral stars or magnetars
    IF(AND(B_classStar.has_a_blue_white_light_spectre, B_classStar.has_a_very_big_mass, B_classStar.has_ten_million_lyfecicle),
       THEN(B_classStar.conclusion)),
    IF(OR(A_classStar.has_impressive_mass, B_classStar.has_a_very_big_mass),
       THEN(AND(A_classStar.conclusion, B_classStar.conclusion))),
   #stars that will end up in black wholes
    IF(AND(O_classStars.has_a_blue_spectre, O_classStars.has_huge_mass, O_classStars.has_million_lifecycle),
       THEN(O_classStars.conclusion)),
    IF(AND(O_classStars.conclusion, O_classStars.has_a_blue_spectre), THEN(O_classStars.conclusion))
)  
o_class_star_name = "Bernards Star"
STAR_PARAMETERS = (O_classStars.has_a_blue_spectre.replace("?x", o_class_star_name), O_classStars.has_million_lifecycle.replace("?x", o_class_star_name),)
hypothesis = O_classStars.conclusion.replace("?x", o_class_star_name)
back = backward_chain(StarClass_RuleSet, hypothesis)
forward = forward_chain(StarClass_RuleSet, STAR_PARAMETERS)
##back = backward_chain(StarClass_RuleSet, STAR_PARAMETERS)
print(forward)
                    
