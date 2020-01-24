from entites import Commune


c = Commune('c', 1234, 1234, 1234)
dotation_solidarite_rurale = c.dotation_solidarite_rurale(1500, 1500)
print("éligible ?", dotation_solidarite_rurale)
