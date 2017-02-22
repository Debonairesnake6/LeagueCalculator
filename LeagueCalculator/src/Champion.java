/**
 * Created by canad on 2/22/2017.
 */
public class Champion {
    private double hp = 2119.2;
    private double bonushp = 0;
    private double totalhp = hp + bonushp;
    private double hp5 = 21.875;
    private double bonushp5 = 0;
    private double totalhp5 = hp5 + bonushp5;
    private double mp = 977.2;
    private double bonusmp = 0;
    private double totalmp = mp + bonusmp;
    private double mp5 = 19.6;
    private double bonusmp5 = 0;
    private double totalmp5 = mp5 + bonusmp5;
    private double ad = 104.04;
    private double bonusad = 0;
    private double totalad = ad + bonusad;
    private double as = 0.878;
    private double bonusas = 0;
    private double totalas = as + bonusas;
    private double arm = 87.248;
    private double bonusarm = 0;
    private double totalarm = arm + bonusarm;
    private double mr = 53.35;
    private double bonusmr = 0;
    private double totalmr = mr + bonusmr;
    private double ms = 345;
    private int range = 150;
    private double ap = 0;
    private int crit = 0;
    private double cdr = 0;
    private int level = 1;
    private double ls = 0;
    private double leth = 0;
    private double gp10 = 0;
    private double mpen = 0;

    public double getBonushp() {
        return bonushp;
    }

    public void setBonushp(double bonushp) {
        this.bonushp = bonushp;
    }

    public double getTotalhp() {
        setTotalhp(getHp() + getBonushp());
        return totalhp;
    }

    public void setTotalhp(double totalhp) {
        this.totalhp = totalhp;
    }

    public double getBonushp5() {
        return bonushp5;
    }

    public void setBonushp5(double bonushp5) {
        this.bonushp5 = bonushp5;
    }

    public double getTotalhp5() {
        setTotalhp5(getHp5() + getBonushp5());
        return totalhp5;
    }

    public void setTotalhp5(double totalhp5) {
        this.totalhp5 = totalhp5;
    }

    public double getBonusmp() {
        return bonusmp;
    }

    public void setBonusmp(double bonusmp) {
        this.bonusmp = bonusmp;
    }

    public double getTotalmp() {
        setTotalmp(getMp() + getBonusmp());
        return totalmp;
    }

    public void setTotalmp(double totalmp) {
        this.totalmp = totalmp;
    }

    public double getBonusmp5() {
        return bonusmp5;
    }

    public void setBonusmp5(double bonusmp5) {
        this.bonusmp5 = bonusmp5;
    }

    public double getTotalmp5() {
        setTotalmp5(getMp5() + getBonusmp5());
        return totalmp5;
    }

    public void setTotalmp5(double totalmp5) {
        this.totalmp5 = totalmp5;
    }

    public double getBonusad() {
        return bonusad;
    }

    public void setBonusad(double bonusad) {
        this.bonusad = bonusad;
    }

    public double getTotalad() {
        setTotalad(getAd() + getBonusad());
        return totalad;
    }

    public void setTotalad(double totalad) {
        this.totalad = totalad;
    }

    public double getBonusas() {
        return bonusas;
    }

    public void setBonusas(double bonusas) {
        this.bonusas = bonusas;
    }

    public double getTotalas() {
        setTotalas(getAs() + getBonusas());
        return totalas;
    }

    public void setTotalas(double totalas) {
        this.totalas = totalas;
    }

    public double getBonusarm() {
        return bonusarm;
    }

    public void setBonusarm(double bonusarm) {
        this.bonusarm = bonusarm;
    }

    public double getTotalarm() {
        setBonusarm(getArm() + getBonusarm());
        return totalarm;
    }

    public void setTotalarm(double totalarm) {
        this.totalarm = totalarm;
    }

    public double getBonusmr() {
        return bonusmr;
    }

    public void setBonusmr(double bonusmr) {
        this.bonusmr = bonusmr;
    }

    public double getTotalmr() {
        setTotalmr(getMr() + getBonusmr());
        return totalmr;
    }

    public void setTotalmr(double totalmr) {
        this.totalmr = totalmr;
    }

    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }

    public double getLs() {
        return ls;
    }

    public void setLs(double ls) {
        this.ls = ls;
    }

    public double getLeth() {
        return leth;
    }

    public void setLeth(double leth) {
        this.leth = leth;
    }

    public double getGp10() {
        return gp10;
    }

    public void setGp10(double gp10) {
        this.gp10 = gp10;
    }

    public double getMpen() {
        return mpen;
    }

    public void setMpen(double mpen) {
        this.mpen = mpen;
    }

    public Champion() {
    }

    public double getCdr() {
        return cdr;
    }

    public void setCdr(double cdr) {
        if (cdr <= 40.0)
            this.cdr = cdr;
        else
            this.cdr = 40;
    }

    public double getHp5() {
        return hp5;
    }

    public void setHp5(double hp5) {
        this.hp5 = hp5;
    }

    public double getMp() {
        return mp;
    }

    public void setMp(double mp) {
        this.mp = mp;
    }

    public double getMp5() {
        return mp5;
    }

    public void setMp5(double mp5) {
        this.mp5 = mp5;
    }

    public double getAd() {
        return ad;
    }

    public void setAd(double ad) {
        this.ad = ad;
    }

    public double getAs() {
        return as;
    }

    public void setAs(double as) {
        this.as = as;
    }

    public double getArm() {
        return arm;
    }

    public void setArm(double arm) {
        this.arm = arm;
    }

    public double getMr() {
        return mr;
    }

    public void setMr(double mr) {
        this.mr = mr;
    }

    public int getRange() {
        return range;
    }

    public void setRange(int range) {
        this.range = range;
    }

    public double getMs() {
        return ms;
    }

    public void setMs(double ms) {
        this.ms = ms;
    }

    public double getAp() {
        return ap;
    }

    public void setAp(double ap) {
        this.ap = ap;
    }

    public int getCrit() {
        return crit;
    }

    public void setCrit(int crit) {
        if (crit <= 100)
            this.crit = crit;
        else
            this.crit = 100;
    }

    public double getHp() {
        return hp;
    }

    public void setHp(double hp) {
        this.hp = hp;
    }
}
