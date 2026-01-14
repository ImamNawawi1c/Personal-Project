package medicinereminder;

public class ObatTablet extends Obat {

    public ObatTablet(String nama, String jam) {
        super(nama, jam);
    }

    @Override
    public String getTipe() {
        return "Tablet";
    }
}
