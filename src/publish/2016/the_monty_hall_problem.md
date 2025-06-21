# The Monty Hall Problem
You've seen it in the movies or read about it in the books: the Monty Hall Problem. The premise is such: you are on a game show. There's three doors, behind one is a prize. Behind the other two is nothing besides disappointment. You pick an arbitrary door. The game host, Monty Hall, opens one of the other doors and reveals that there is no prize behind it. Keeping the other two doors closed, he asks you if you would like to switch your choice or remain with your original pick. What should you do? Ben Campbell has a solution.

https://www.youtube.com/watch?v=CYyUuIXzGgI

You're meaning to tell me that if I switch mid-game, an offer by the man who set up all the doors and the respective prizes, I would have a better chance of winning? How is this possible? Seems a bit counterintuitive. Seems almost wrong. Fortunately, we can test this with a simple program. 

```swift
import Darwin // for arc4random_uniform

func random(from from: Int, to: Int, except: Array<Int>? = nil) -> Int {
    let number = Int(arc4random_uniform(UInt32(to - from + 1))) + from // produce bounds, +1 to make inclusive
    
    if except != nil && except?.indexOf(number) != nil {
        return random(from: from, to: to, except: except) // recursively call until you find the a number that doesn't contain the value
    }
    
    return number
}

// returns if you won when you stayed and switched, respectively
func montyHall(doors: Int) -> (Bool, Bool) {
    let originalDoor = random(from: 1, to: doors) // Your original choice
    let correctDoor = random(from: 1, to: doors) // The winning choice.
    
    let revealedDoor = random(from: 1, to: doors, except: [correctDoor, originalDoor]) // The door the judge reveals
    let switchedDoor = random(from: 1, to: doors, except: [revealedDoor, originalDoor]) // Supposing you switched, you woudl
    
    return (originalDoor == correctDoor, switchedDoor == correctDoor)
}

let testValues = [100, 1_000, 10_000, 100_000, 1_000_000, 1_000_000]
let actualNumberOfDoors = 3

for value in testValues {
    var stayingCounter = 0, switchingCounter = 0
    
    for _ in 0...value {
        let (stayedWon, switchedWon) = montyHall(actualNumberOfDoors)
        if stayedWon { stayingCounter += 1 }
        if switchedWon { switchingCounter += 1 }
    }
    
    print("Test Case: \(value). Staying Won: \(stayingCounter), Switching Won: \(switchingCounter)")
}
```

There's no tricks in the code. No gimmicks. So, the results?

<table>
  <tr>
    <th>Input</th>
    <th>Staying Won</th>
    <th>Switching Won</th>
  </tr>
  <tr>
    <td>100</td>
    <td>42</td>
    <td>58</td>
  </tr>
  <tr>
    <td>1000</td>
    <td>344</td>
    <td>656</td>
  </tr>
  <tr>
    <td>10000</td>
    <td>3289</td>
    <td>6711</td>
  </tr>
  <tr>
    <td>100000</td>
    <td>33203</td>
    <td>66797</td>
  </tr>
  <tr>
    <td>1000000</td>
    <td>333178</td>
    <td>666822</td>
  </tr>
  <tr>
    <td>10000000</td>
    <td>3335146</td>
    <td>6664854</td>
  </tr>
</table>

It appears that Ben[^1] was right. Taking the limit as the input get higher,  switching won roughly $66\%$ of the time — compared that to the original $33\%$ you got before you were given the option to switch doors. So, how is this possible? I'll explain.

For simplicity, suppose the prize is behind door A out of doors A, B, C. The argument can be made for any initial door, but A makes it easier. At this point, you have $\frac{1}{3}$ chance of picking the prize no matter what you pick. If you pick door A, the door which contains the prize, the host will definitely want you to change so he will offer you either door B or C. Now suppose you choose a door without the prize, either door B or C. The host has *no choice* but to *eliminate the door without the prize*. Meaning if you switch, you have the winning door.

So, why $66\%$? Computationally, if you always switch and you picked the wrong door initially, your switch will win every time. There's two incorrect choices out of three, meaning $\frac{2}{3}$ of the time you will win. 

You've just had your first lesson in conditional probability.


[^1]:	21 main character, played by Jim Sturgess