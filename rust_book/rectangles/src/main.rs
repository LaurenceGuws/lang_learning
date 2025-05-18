#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&mut self) -> u32 {
        self.height * {self.width + 1}
    }
    fn can_hold(&self, not_self: &Rectangle) -> bool {
        self.width > not_self.width && self.height > not_self.height
    }
    fn square (size: u32) -> Self {
        Self{
            width: size,
            height: size,
        }
    }
}

fn main() {
    let mut rect1 = Rectangle {
        width: dbg!(30*2),
        height: 50,
    };
    let rect4 = Rectangle::square(10);

    let rect2 = Rectangle{
        width: {&rect1.width / 2},
        height: {&rect1.height / 2},
    };
    let rect3 = Rectangle{
        width: {&rect1.width * 2},
        height: {&rect1.height * 2},
    };
    println!("The are of the rectangle is {} square pixels.",
        rect1.area()
    );
    dbg!(&rect1);
    println!("rect1 is: {rect1:#?}");
    println!("rect1 can contain rect2: {}", rect1.can_hold(&rect2));
    println!("rect1 can contain rect3: {}", rect1.can_hold(&rect3));
    println!("rect1 can contain rect4: {}", rect1.can_hold(&rect4));
}
