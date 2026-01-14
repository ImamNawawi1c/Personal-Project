package medicinereminder;

public abstract class Obat {
    protected String nama;
    protected String jam;

    public Obat(String nama, String jam) {
        this.nama = nama;
        this.jam = jam;
    }

    public String getNama() {
        return nama;
    }

    public String getJam() {
        return jam;
    }

    public abstract String getTipe();
}
