from fnmatch import fnmatch

def run(name, hp, hp5, mp, mp5, ad, atkspd, arm, mr, range, ms, ap, crit, cdr, passive, ls, leth, gp10, mpen, basead, msper):
    file = open ("D:\Desktop\League Calculator Repo\ItemCode.txt", "a+")
    file.write("\tpublic String[] " + name + "() {\n")

    if not hp == 0:
        file.write("\t\tchamp.setBonushp(champ.getBonushp() + " + hp + ");\n")

    if not hp5 == 0:
        file.write("\t\tchamp.setBonushp5(champ.getBonushp5() + " + hp5 + ");\n")

    if not mp == 0:
        file.write("\t\tchamp.setBonusmp(champ.getBonusmp() + " + mp + ");\n")

    if not mp5 == 0:
        file.write("\t\tchamp.setBonusmp5(champ.getBonusmp5() + " + mp5 + ");\n")

    if not ad == 0:
        file.write("\t\tchamp.setBonusad(champ.getBonusad() + " + ad + ");\n")

    if not atkspd == 0:
        file.write("\t\tchamp.setBonusas(champ.getBonusas() + " + atkspd + ");\n")

    if not arm == 0:
        file.write("\t\tchamp.setBonusarm(champ.getBonusarm() + " + arm + ");\n")

    if not mr == 0:
        file.write("\t\tchamp.setBonusmr(champ.getBonusmr() + " + mr + ");\n")

    if not range == 0:
        file.write("\t\tchamp.setRange(champ.getRange() + " + range + ");\n")

    if not ms == 0:
        file.write("\t\tchamp.setMs(champ.getMs() + " + ms + ");\n")

    if not ap == 0:
        file.write("\t\tchamp.setAp(champ.getAp() + " + ap + ");\n")

    if not crit == 0:
        file.write("\t\tchamp.setCrit(champ.getCrit() + " + crit + ");\n")

    if not cdr == 0:
        file.write("\t\tchamp.setCdr(champ.getCdr() + " + cdr + ");\n")

    if not ls == 0:
        file.write("\t\tchamp.setLs(champ.getLs() + " + ls + ");\n")

    if not leth == 0:
        file.write("\t\tchamp.setLeth(champ.getLeth() + " + leth + ");\n")

    if not gp10 == 0:
        file.write("\t\tchamp.setGp10(champ.getGp10() + " + gp10 + ");\n")

    if not mpen == 0:
        file.write("\t\tchamp.setMpen(champ.getMpen() + " + mpen + ");\n")

    if not basead == 0:
        file.write("\t\tchamp.setAd(champ.getAd() + (1 + " + str(float(basead) / 100) + "));\n")

    if not msper == 0:
        file.write("\t\tchamp.setMs(champ.getMs() * (1 + " + str(float(msper) / 100) + "));\n")

    if not passive[0] == '0':
        size = 0
        for line in passive:
            if not line == '0':
                size += 1

        file.write("\t\tString [] passive = new String[" + str(size) + "];\n")
        count = 0
        for line in passive:
            if not line == '0':
                file.write("\t\tpassive[" + str(count) + "] = \"" + line + "\";\n")
                count += 1
    else:
        file.write("\t\tString[] passive = new String[1];\n")
        file.write("\t\tpassive[0] = \"none\";\n")

    file.write(("\t\treturn passive;\n\t}\n"))

    file.close()

if __name__ == '__main__':
    file = open("D:\Desktop\League Calculator Repo\ItemCode.txt", "w+")
    file.close()
    name = 'test'
    nextname = 0
    hp = 0
    hp5 = 0
    mp = 0
    mp5 = 0
    ad = 0
    atkspd = 0
    arm = 0
    mr = 0
    range = 0
    ms = 0
    ap = 0
    crit = 0
    cdr = 0
    ls = 0
    leth = 0
    gp10 = 0
    mpen = 0
    basead = 0
    msper = 0
    passive = ['0','0','0']
    passivenext = 0

    list = open ("D:\Desktop\League Calculator Repo\List.txt", "r")
    for line in list:
        line = line.strip()
        if line == 'Name:':
            nextname = 1
        elif nextname == 1:
            name = line
            nextname = 0
        elif line == '---':
            run(name, hp, hp5, mp, mp5, ad, atkspd, arm, mr, range, ms, ap, crit, cdr, passive, ls, leth, gp10, mpen,
                basead, msper)
            name = 'test'
            hp = 0
            hp5 = 0
            mp = 0
            mp5 = 0
            ad = 0
            atkspd = 0
            arm = 0
            mr = 0
            range = 0
            ms = 0
            ap = 0
            crit = 0
            cdr = 0
            ls = 0
            leth = 0
            gp10 = 0
            mpen = 0
            basead = 0
            msper = 0
            passive = ['0','0','0']
            passivenext = 0
        elif fnmatch (line, "* HP"):
            copy = line.split(' ')
            hp = copy[0]
        elif fnmatch(line, "* HPRgn"):
            copy = line.split(' ')
            hp5 = copy[0]
        elif fnmatch(line, "* MP"):
            copy = line.split(' ')
            mp = copy[0]
        elif fnmatch(line, "* MPRgn"):
            copy = line.split(' ')
            mp5 = copy[0]
        elif fnmatch(line, "* AD"):
            copy = line.split(' ')
            ad = copy[0]
        elif fnmatch(line, "* AS"):
            copy = line.split(' ')
            atkspd = copy[0]
        elif fnmatch(line, "* AR"):
            copy = line.split(' ')
            arm = copy[0]
        elif fnmatch(line, "*% MS"):
            copy = line.split('%')
            msper = copy[0]
        elif fnmatch(line, "* MR"):
            copy = line.split(' ')
            mr = copy[0]
        elif fnmatch(line, "* MS"):
            copy = line.split(' ')
            ms = copy[0]
        elif fnmatch(line, "* AP"):
            copy = line.split(' ')
            ap = copy[0]
        elif fnmatch(line, "* Crit"):
            copy = line.split(' ')
            crit = copy[0]
        elif fnmatch(line, "* CDR"):
            copy = line.split(' ')
            cdr = copy[0]
        elif fnmatch(line, "* LS"):
            copy = line.split(' ')
            ls = copy[0]
        elif fnmatch(line, "* Lethality"):
            copy = line.split(' ')
            leth = copy[0]
        elif fnmatch(line, "* GP10"):
            copy = line.split(' ')
            gp10 = copy[0]
        elif fnmatch(line, "* Mpen"):
            copy = line.split(' ')
            mpen = copy[0]
        elif fnmatch(line, "* baseAD"):
            copy = line.split('%')
            basead = copy[0]
        elif fnmatch(line, "Passive*"):
            passivenext = 1
        elif passivenext == 1:
            if passive[0] == '0':
                passive[0] = line
            elif passive[1] == '0':
                passive[1] = line
            else:
                passive [2] = line