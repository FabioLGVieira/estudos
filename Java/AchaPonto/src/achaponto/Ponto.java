
package achaponto;

public class Ponto {
    private int axisX,axisY;

    public Ponto(int axisX, int axisY) {
        this.axisX = axisX;
        this.axisY = axisY;
    }

    public int getAxisX() {
        return axisX;
    }

    public void setAxisX(int axisX) {
        this.axisX = axisX;
    }

    public int getAxisY() {
        return axisY;
    }

    public void setAxisY(int axisY) {
        this.axisY = axisY;
    }
    
    @Override
    public String toString(){
        
        return this.axisX + "," + this.axisY;
    }
    
}
