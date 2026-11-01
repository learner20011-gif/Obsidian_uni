![[Pasted image 20261031222500.png]]![[Pasted image 20261031223438.png]]![[Pasted image 20261031224503.png]]![[Pasted image 20261031225436.png]]![[Pasted image 20261101214449.png]]
![[Pasted image 20261101194040.jpg]]
![[Pasted image 20261101200548.png|658]]![[Pasted image 20261101200648.png|675]]![[Pasted image 20261101201005.png]]![[Pasted image 20261101200805.png|678]]![[Pasted image 20261101203546.png]]
![[Pasted image 20261101203606.png]]
![[Pasted image 20261101204207.png]]
![[Pasted image 20261101204403.png|674]]![[Pasted image 20261101213014.png]]![[Pasted image 20261101215752.png]]![[Pasted image 20261101213607.png]]
#### AOI222 (AND-OR-INVERT 2-2-2)

- **Boolean Expression:**
    

$$Y = \overline{(A \cdot B) + (C \cdot D) + (E \cdot F)}$$

#### Boolean Expression of OAI322

$$Y = \overline{(A + B + C)(D + E)(F + G)}$$

#### OA322 (Non-Inverting Version of OAI322)

- **Boolean Expression:**
    

$$Y = (A + B + C)(D + E)(F + G)$$

| **Feature**         | **Contact Cut**                                 | **Via**                                   |
| ------------------- | ----------------------------------------------- | ----------------------------------------- |
| **Connection Type** | Metal-to-Silicon (Metal-1 to Poly or Diffusion) | Metal-to-Metal (e.g., Metal-1 to Metal-2) |
| **Position**        | Lowest interconnect level                       | Upper interconnect levels                 |
#### Why Poly Overhangs by $2\lambda$

- **Prevents Short Circuits:** Without an overhang, mask misalignment would leave the channel exposed during implantation, shorting source to drain.
    
- **Safety Margin:** The $2\lambda$ extension guarantees full channel coverage even if layers shift slightly during fabrication.