package medicinereminder;

import java.util.ArrayList;

public class MedicineManager {

    private ArrayList<Obat> daftarObat = new ArrayList<>();

    public void tambahObat(Obat obat) {
        daftarObat.add(obat);
    }

    public ArrayList<Obat> getDaftarObat() {
        return daftarObat;
    }
}
