import unittest


from entity import Entity
from weapon import Weapon
from hero import Hero
from orc import Orc
from fight import Fight


class EntityTest(unittest.TestCase):
    
    def test_entity_name(self):
        new_entity = Entity("Nametest", 100)
        self.assertEqual('Nametest', new_entity.name)
        
    def test_wrong_name(self):
        self.assertRaises(ValueError, lambda: Entity("123", 100))
        
    def test_wrong_name2(self):
        self.assertRaises(ValueError, lambda: Entity("", 100))
        
    def test_wrong_name3(self):
        self.assertRaises(TypeError, lambda: Entity(100, 100))
        
    def test_entity_health(self):
        new_entity = Entity("Healthtest", 100)
        self.assertEqual(100, new_entity.health)
        
    def test_wrong_health(self):
        self.assertRaises(ValueError, lambda: Entity("minus", -1))
        
    def test_wrong_health2(self):
        self.assertRaises(ValueError, lambda: Entity("name", "iddqd"))
        
    def test_taking_damage(self):
        new_entity = Entity("damageinc", 100)
        new_entity.take_damage(10)
        self.assertEqual(90, new_entity.health)
        
    def test_healing_max_health(self):
        new_entity = Entity("healingco", 100)
        new_entity.take_healing(10)
        self.assertEqual(100, new_entity.health)
        
    def test_healing_when_damaged(self):
        new_entity = Entity("patchwork", 100)
        new_entity.take_damage(10)
        new_entity.take_healing(5)
        self.assertEqual(95, new_entity.health)
    
    def test_healing_when_damaged_and_max_health(self):
        new_entity = Entity("patchwork", 100)
        new_entity.take_damage(10)
        new_entity.take_healing(50)
        self.assertEqual(100, new_entity.health)
        
    def test_healing_when_dead(self):
        new_entity = Entity("raisedead", 100)
        new_entity.take_damage(100)
        self.assertFalse(new_entity.take_healing(10))
    
    def test_is_alive(self):
        new_entity = Entity("alive", 100)
        self.assertTrue(new_entity.is_alive())
        
    def test_is_alive2(self):
        new_entity = Entity("aliveagain", 100)
        new_entity.take_damage(10)
        self.assertTrue(new_entity.is_alive())
        
    def test_is_dead(self):
        new_entity = Entity("Deadmeat", 100)
        new_entity.take_damage(100)
        self.assertFalse(new_entity.is_alive())
        
    def test_overkill(self):
        new_entity = Entity("Overkill", 100)
        new_entity.take_damage(101)
        self.assertFalse(new_entity.is_alive())
    
    def test_has_weapon(self):
        new_entity = Entity("EdwardBarehands", 100)
        self.assertFalse(new_entity.has_weapon())
        
    def test_equip_weapon(self):
        new_entity = Entity("equip", 100)
        axe = Weapon("skullsplitter", 10, 1.2)
        new_entity.equip_weapon(axe)
        self.assertTrue(new_entity.has_weapon())
        
    def test_switch_weapon(self):
        new_entity = Entity("equipswitch", 100)
        axe = Weapon("skullsplitter", 10, 0.2)
        bow = Weapon("arrowless bow", 1, 1.0)   
        new_entity.equip_weapon(axe)
        new_entity.equip_weapon(bow)
        self.assertEqual(new_entity.weapon.name, bow.name)


class HeroTest(unittest.TestCase):
    
    def test_notoriety(self):
        new_hero = Hero("Jack", 100, "Ripper")
        self.assertEqual(new_hero.known_as(), "Jack the Ripper")


class OrcTest(unittest.TestCase):

    def test_berserk_factor(self):
        new_orc = Orc("Gruumsh", 100, 1.3)
        self.assertEqual(new_orc.berserk_factor, 1.3)
        
    def test_berserk_factor_low(self):
        new_orc = Orc("Gruumsh", 100, 0.1)
        self.assertEqual(new_orc.berserk_factor, 1.0)
    
    def test_berserk_factor_high(self):
        new_orc = Orc("Gruumsh", 100, 10.0)
        self.assertEqual(new_orc.berserk_factor, 2.0)

    def test_berserk_factor_int(self):
        new_orc = Orc("Gruumsh", 100, 1)
        self.assertEqual(new_orc.berserk_factor, 1.0)
        
    def test_berserk_factor_type(self):
        self.assertRaises(TypeError, lambda: Orc("Gruumsh", 100, "catch!"))
        
    def test_gone_berserk(self):
        new_orc = Orc("Gruumsh", 100, 1.4)
        new_orc.take_damage(41)
        new_orc.get_health()
        self.assertTrue(new_orc.go_berserk())
    
    def test_not_gone_berserk(self):
        new_orc = Orc("Gruumsh", 100, 1.4)
        new_orc.take_damage(40)
        new_orc.get_health()
        self.assertFalse(new_orc.go_berserk())


class WeaponTest(unittest.TestCase):
    
    def test_weapon_nametype(self):
        self.assertRaises(TypeError, lambda: Weapon(101, 10, 1.0))
    
    def test_weapon_damagetype(self):
        self.assertRaises(TypeError, lambda: Weapon("herosmasher", "10", 1.0))
    
    def test_weapon_crittype(self):
        self.assertRaises(TypeError, lambda: Weapon("herosmasher", 10, "always"))
        
    def test_weapon_critical_hit(self):
        new_weapon = Weapon("alwayscrit", 10, 1)
        for i in range(0, 10):
            iscrit = new_weapon.critical_hit()
            if not iscrit:
                break
        self.assertTrue(iscrit)

    def test_weapon_no_crit(self):
        new_weapon = Weapon("alwayscrit", 10, 0)
        for i in range(0, 1000):
            iscrit = new_weapon.critical_hit()
            if iscrit:
                break
        self.assertFalse(iscrit)


class FightTest(unittest.TestCase):
    def test_fight1(self):
        new_hero = Hero("Jack", 100, "Ripper")
        new_orc = Orc("Gruumsh", 40, 1.2)
        hero_weapon = Weapon("The Sting", 8, 0.33)
        orc_weapon = Weapon("The Pacifier", 12, 1)
        new_hero.equip_weapon(hero_weapon)
        new_orc.equip_weapon(orc_weapon)
        Fight(new_hero, new_orc)

if __name__ == '__main__':
    unittest.main()
