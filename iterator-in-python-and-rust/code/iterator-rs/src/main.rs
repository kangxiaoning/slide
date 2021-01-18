struct AlphaList<T> {
    alpha_list: Vec<T>,
}

impl<T> AlphaList<T> {
    pub fn new(elements: Vec<T>) -> Self {
        AlphaList {
            alpha_list: elements,
        }
    }
}

struct AlphaListIterator<T> {
    alpha_list: Vec<T>,
    index: usize,
}

impl<T> Iterator for AlphaListIterator<T>
where
    T: Clone,
{
    type Item = T;
    fn next(&mut self) -> Option<Self::Item> {
        match self.alpha_list.get(self.index) {
            Some(e) => {
                self.index += 1;
                return Some(e.clone());
            }
            None => return None,
        }
    }
}

impl<T> IntoIterator for AlphaList<T>
where
    T: Clone,
{
    type Item = T;
    type IntoIter = AlphaListIterator<T>;

    fn into_iter(self) -> Self::IntoIter {
        AlphaListIterator {
            alpha_list: self.alpha_list,
            index: 0,
        }
    }
}

fn main() {
    let alpha_list = AlphaList::new(vec![1, 2, 3]);
    for e in alpha_list {
        println!("{}", e);
    }
}
