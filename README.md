# Nullscape (ROBLOX) Manual APWorld
### **<ins>By StudMuffin and sucrosesnowstorm</ins>**

Manual APWorld for Nullscape \[DOOM IN BLOOM]. Recommended to have most if not all classes unlocked.

As of v1.0.0, traps are included by default and are non-customizable. This will be fixed in the future, but this is Manual so ignore it if you don't want to deal with em.
ignore filler_traps, it's like a weird spirit haunting our apworld.


</br></br>


## "gimme a quick summary"
Players start with all classes (but one) locked, may not purchase any upgrades, and cannot access Level 5 and beyond until unlocking each as [items](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#progression). All Upgrades are spread into six sets of "[Seeds](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#upgrades)", which each are progressive unlocks for a certain *category* of Upgrade (e.g. the 3rd *Seed of Control* unlocks purchasing Double Jump).
The goal is to reach a set "final level" with a class that you have its respective "[ROOTS](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#bloom)" item in (optional) and a prerequisite amount of "[*FRAGMENT OF BLOSSOM*](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#bloom)" (also optional, usually 20 of 30 total).



</br></br></br>



## YAML OPTIONS


- ***Randomize Lategame Upgrades*** (`randomize_lategame_upgrades`, default: `true`)
> By default, all obtainable upgrades are randomized as Seeds. Disable to exclude upgrades that only appear at Level 15 or later. Upgrades excluded by this option are written in italics in the [Item Codex](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#upgrades).

- ***Randomize Difficulty Selection*** (`randomize_lower_difficulty`, default: `true`)
> Adds 2 '[Progressive Lower Difficulty](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#progression)'s. When included, the player starts on Extreme, and can lower difficulty when the items are collected.

- ***Starting Class*** (`starting_class`, default: `prisoner`, other choices: `wanted`, `charger`, `glider`, `grappler`, `spirit`, and `diver`)
> Choose which class the player starts with.

- ***goal*** (`goal`, default: `reach level 10`, other choices: `reach level 15` and `reach level 20`)
> What do you need to do to win this APWorld, once meeting all other requirements.

- ***Total FRAGMENT OF BLOSSOM*** (`total_blossom_fragments`, default: `30`, range of `0`-`40`)
> How many [FRAGMENT OF BLOSSOM](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#bloom) are randomized.

- ***FRAGMENT OF BLOSSOM required*** (`blossom_fragments_required`, default: `20`, range of `0`-`40`)
> How many [FRAGMENT OF BLOSSOM](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#bloom) are required to goal. (Recommened to be ~10 less than total).

- ***Randomize ROOTS*** (`randomize_roots`, default: `true`)
> Include a ROOTS item for each class, which are a requirement for a class to goal. See [summary](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#gimme-a-quick-summary) and [Item Codex](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#bloom) for more info.

- ***Classes Excluded*** (`classSelect`, default: none)
> Exclude specific classes from the randomizer (except Charger/Diver).
> These are "`Grappler`", "`Spirit`", "`Glider`", "`Prisoner`", and "`Wanted`" (case sensitive).
> Each class contains a significant amount of locations, so avoid removing too many without also removing items to compensate.


</br></br>



## ITEM CODEX


### <ins>*Upgrades*</ins>

- ***Seed of Potential*** (Progression): Progressive Economy Upgrades
> 1) Paycheck
> 2) Business Liscense
> 3) Medal
> 4) Fanny Pack
> 5) *Gift Magnet*
> 6) *Gift Idol*
- ***Seed of Control*** (Progression): Progressive Mobility Upgrades
> 1) Adrenaline
> 2) Swiftness Rings
> 3) Double Jump
> 4) Grace Wings
> 5) Pocket Bell
> 6) Ice Skates
> 7) Advanced Gravity Coil
> 8) *Sport Shoes*
> 9) *Matrix Tetrahedron*
- ***Seed of Nullscape*** (Progression): Progressive World Upgrades
> 1) Better Jump Pads
> 2) Grapple Points
> 3) Tria Orbs
> 4) More Altars
> 5) Larger Grapple Points
- ***Seed of Introspection*** (Progression): Progressive Class-Specific Upgrades
> 1) Helmet
> 2) Ninja Belt
> 3) *Shark Tail*
> 4) *Miniature Hourglass*
- ***Seed of Omnipotence*** (Useful): Progressive Radar
> 1) Radar
> 2) Radar Module: Enemies
> 3) Radar Module: Tripmines
> 4) Radar Module: Altars
> 5) Radar Module: Players
> 6) *Radar Module: Instruments*
- ***Seed of Immortality*** (Progression): Progressive Defense Upgrades
> 1) Defuse Kit
> 2) Last Robloxian Standing
> 3) Subspacial Barrier
> 4) *Shield*
> 5) *Panic Necklace*
> 6) *Drowned Aegis*
- ***Extra Upgrade Stack*** (Useful): You may purchase an extra stack of any Upgrade for each copy of this item you have. 4 copies. </br>

### <ins>*Progression*</ins>

- ***Progressive Ungate Levels*** (Progression): Unlock Levels past 4
> 1) Ungate Levels 5-9
> 2) Ungate Levels 10-14
> 3) Ungate Levels 15-19
> 4) Ungate All Levels
- ***Progressive Lower Difficulty*** (Progression): Unlock difficulties lower than Extreme. [Can be excluded](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#yaml-options) to allow play on any difficulty.
> 1) Standard Difficulty
> 2) Casual Difficulty </br>

### <ins>*Class Unlocks*</ins>

- ***Diver Class*** (Progression): Unlock Diver. [May be given by default if set to be so](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#yaml-options).
- ***Charger Class*** (Progression): Unlock Charger. [May be given by default if set to be so](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#yaml-options).
- ***Grappler Class*** (Progression): Unlock Grappler. [May be given by default or excluded if set to be so](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#yaml-options).
- ***Spirit Class*** (Progression): Unlock Spirit. [May be given by default or excluded if set to be so](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#yaml-options).
- ***Glider Class*** (Progression): Unlock Glider. [May be given by default or excluded if set to be so](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#yaml-options).
- ***Prisoner Class*** (Progression): Unlock Prisoner. [May be given by default or excluded if set to be so](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#yaml-options).
- ***Wanted Class*** (Progression): Unlock Wanted. [May be given by default or excluded if set to be so](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#yaml-options). </br>

### <ins>*Traps*</ins>

###### (As always with Manual traps, feel free to reinterpret each trap however you wish. The listed effects are just our recommendation.)
- ***Flesh Trap*** (Trap): You may not use your ability next level.
- ***Oblivion Trap*** (Trap): You may not use extra jumps next level.
- ***Prisoner Trap*** (Trap): You may use neither extra jumps nor your ability next level. </br>

### <ins>*No Category*</ins>
- ***ummm you get \*nothing\*! lol*** (Filler): you're gonna have to guess what this one does. </br>

### <ins>*BLOOM.*</ins>

- ***ROOTS IN VERSATILITY*** (Progression): Allow the player to select Diver as their class of choice when aiming to goal. [Can be excluded](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#yaml-options).
- ***ROOTS IN PERSISTENCE*** (Progression): Allow the player to select Charger as their class of choice when aiming to goal. [Can be excluded](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#yaml-options).
- ***ROOTS IN TRUST*** (Progression): Allow the player to select Grappler as their class of choice when aiming to goal. [Can be excluded](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#yaml-options).
- ***ROOTS IN SELF-AWARENESS*** (Progression): Allow the player to select Spirit as their class of choice when aiming to goal. [Can be excluded](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#yaml-options).
- ***ROOTS IN BRAVERY*** (Progression): Allow the player to select Glider as their class of choice when aiming to goal. [Can be excluded](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#yaml-options).
- ***ROOTS IN CERTAINTY*** (Progression): Allow the player to select Prisoner as their class of choice when aiming to goal. [Can be excluded](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#yaml-options).
- ***ROOTS IN DEFIANCE*** (Progression): Allow the player to select Wanted as their class of choice when aiming to goal. [Can be excluded](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#yaml-options).
- ***FRAGMENT OF BLOSSOM*** (Progression): Allow the player to attempt to goal if a certain threshold of duplicates are acquired. Total amount, and amount required to goal will vary on [player preference](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#yaml-options). [Can be excluded](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#yaml-options). </br>


</br></br>


## LOCATIONS CODEX


### <ins>*Any Class*</ins>
###### Can be completed as any class.

- ***Encounter Voidbound Enemy***: Be in the same level as a Voidbound Baby, Voidbound Operator, or Voidbound Guardian.
- ***Survive Voidbreaker Encounter***: Have a Voidbreaker attack you and still be alive when it disappears.
- ***3 Husk Curses***: Have 3 Husk curses active at the same time.
- ***2 Tripmine Curses***: Have 2 Tripmine curses active at the same time. Duplicates of the same curse count as separate.
- ***Greater Curse***: Have an active greater curse.
- ***Burn***: Be afflicted with *Burn*. This can be caused by ICBMs with *Scorched Earth* or through the chimneys of high-rise towers.
- ***Become Concussed***: Be afflicted with *Concussion (effect)*. This can be caused by Bells with *Concussion (curse)* or Springers with *Concussion (curse)* and *Resonating Shockwaves*
- ***Escape With Spare Shield***: Enter the beacon while still having a shield for any reason.
- ***Escape With Spare Subspacial Barrier***: Enter the beacon with a *Subspacial Barrier* that has yet to be used this level.
- ***Seamine Curse***: Have an active curse affecting seamines.
- ***Kolóna Curse***: Have an active Kolóna curse.</br>

### <ins>*Each Class*</ins>
###### Exists as identical quests that must be checked as each class individually.

- ***Reach Level 5***: Enter the Level 5 intermission. Until you collect a [*Progressive Ungate Levels*](https://github.com/sucrosesnowstorm/manual_nullscaperoblox_sucrosesnowstorm#progression) all locations past this point are inaccessible, including curse/enemy picks.
- ***All Gold Gifts***: Collect 100% of a level's gold gifts.
- ***Escape After Complete Destruction (Level 3+)***: Enter the beacon (of a level past 2) only after all tiles have collapsed.
- ***Take Baby***: Take a permanent Baby.
- ***Encounter Flesh***: Be in the same level as a Flesh.
- ***Take Husk***: Take a permanent Husk.
- ***Encounter Telefragger***: Be in the same level as a Telefragger.
- ***Medal Curse***: Using *Medal*, choose to take a Medal Curse.
- ***Altar of Purgatory***: Activate an Altar of Purgatory.
- ***Reach Level 13***: Enter the Level 13 intermission.
- ***Overtuned***: Be afflicted with *Overtuned*. This can be caused by ringing a Bell 3 times in succession, or by a Springer with *Resonating Shockwaves*.
- ***Abilityless Level (Level 3+)***: Complete a level (past 2) without ever using your ability. *Prisoner* and *Wanted* class don't have this check.<br/>

### <ins>*Charger Class*</ins>

- ***Detonate 5 Tripmines In A Level***: Using your ability, destroy 5 tripmines in a single level. Accessible before level 5 in Extreme.
- ***ICBM Curse***: Have an active ICBM curse.
- ***Drop Bounce On Grapple Point***: Using your ability mid-air, land on a grapple point to bounce higher than normal.
- ***Ride Grindrail***: Step on a grindrail. </br>

### <ins>*Diver Class*</ins>

- ***Dive Into Bell***: boing.
- ***Survive A Ninja Belt Bonk***: With *Ninja Belt*, use your alt ability to hit a wall and bonk without falling into the void.
- ***Telefragger Curse***: Have an active Telefragger curse.
- ***Dive Into Grapple Point***: boing(2).</br>

### <ins>*Spirit Class*</ins>

- ***Take Mart And Springer***: Take a permanent Mart and a permanent Springer.
- ***Clear A Gold Tile With A Single Fling***: Collect all gold gifts on a *Fanny Pack*'s gold tile shortly after leaving your spirit form.
- ***Above The Beacon's Clouds***: Using your ability, reach a significant height above the level. The beacon's "clouds" are not always visible, so use your best judgement for a sufficient height.
- ***Chance Curse***: Have an active curse relating to the Altar of Chance.</br>

### <ins>*Grappler Class*</ins>

- ***Disable Jump Pad***: Grapple onto a jump pad enough that it can no longer be grappled to.
- ***Grapple Point Combo***: Use two grapple points without touching the ground.
- ***Seamine Grappler***: Grapple onto a seamine.
- ***Take Flesh And Operator***: Take a permanent Mart and a permanent Operator. </br>

### <ins>*Glider Class*</ins>

- ***Flesh Curse***: Have an active Flesh curse.
- ***Survive A Bonk***: Glide into a wall and bonk without falling into the void.
- ***Glide Into A Grapple Point***: boing(horizontal).
- ***Survive Seamine Detonation***: Cause a seamine to detonate, and survive.</br>

### <ins>*Prisoner Class*</ins>

- ***Take Useless Upgrade***: Buy an upgrade that does nothing. *(Upgrades left unrandomized from Randomize Lategame Upgrades do not count.)*
- ***Take Bell And Springer***: Take a permanent Bell and a permanent Springer
- ***Use Jump Pad***: scary !
- ***Use Altar***: Activate any altar.</br>

### <ins>*Wanted Class*</ins>

- ***Take Husk And ICBM***: Take a permanent Husk and a permanent ICBM
- ***2 Medal Curses***: Have 2 curses gained from *Medal* active at the same time.
- ***Survive Kolóna Encounter***: Remain alive after a Kolóna attack.
- ***Bounce Tourist***: Without touching the ground, use all three of a jump pad, grapple point, and Tria orb.
