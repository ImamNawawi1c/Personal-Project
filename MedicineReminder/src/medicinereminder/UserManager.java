package medicinereminder;

import java.util.ArrayList;
import java.util.List;

public class UserManager {
    private List<User> users = new ArrayList<>();
    
    public UserManager(){
        users.add(new User("admin", "admin"));
    }
    
    public boolean register(String username, String password){
        for (User usr : users){
            if (usr.getUsername().equalsIgnoreCase(username)){
                return false; 
        }
    }
           users.add(new User(username, password));
           return true;
    }
    
    public boolean login(String username , String password) {
        for (User usr : users){
            if (usr.getUsername().equals(password)){
            return true;
         }
        }
        return false;
    }
}    
    

