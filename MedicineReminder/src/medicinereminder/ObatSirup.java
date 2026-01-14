package medicinereminder;

public class ObatSirup extends Obat {

    public ObatSirup(String nama, String jam) {
        super(nama, jam);
    }

    @Override
    public String getTipe() {
        return "Sirup";
    }
}
