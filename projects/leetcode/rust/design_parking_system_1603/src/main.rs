pub struct ParkingSystem {
    big: i32,
    medium: i32,
    small: i32,
}

impl ParkingSystem {

    pub fn new(big: i32, medium: i32, small: i32) -> Self {
        Self {
            big: big,
            medium: medium,
            small: small,
        }
    }
    
    pub fn add_car(&mut self, car_type: i32) -> bool {
        match car_type {
            1 => {
                if self.big > 0 {
                    self.big -= 1;
                    return true;
                } else {
                    return false;
                }
            },
            
            2 => {
                if self.medium > 0 {
                    self.medium -= 1;
                    return true;
                } else {
                    return false;
                }
            },
            
            3 => {
                if self.small > 0 {
                    self.small -= 1;
                    return true;
                } else {
                    return false;
                }
            },
            _ => false
        }
    }
}

