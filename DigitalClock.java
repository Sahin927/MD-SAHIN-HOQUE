import javax.swing.*;
import java.awt.*;
import java.text.SimpleDateFormat;
import java.util.Date;

public class DigitalClock {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Digital Clock");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 200);
        frame.setLayout(new BorderLayout());

        JLabel clockLabel = new JLabel("", SwingConstants.CENTER);
        clockLabel.setFont(new Font("Calibri", Font.BOLD, 40));
        clockLabel.setBackground(Color.BLACK);
        clockLabel.setForeground(Color.WHITE);
        clockLabel.setOpaque(true);

        frame.add(clockLabel, BorderLayout.CENTER);
        frame.setVisible(true);

        // Method to update the clock and date
        Timer timer = new Timer(1000, e -> updateTime(clockLabel));
        timer.start();
    }

    // Function to update time and date on the label
    private static void updateTime(JLabel clockLabel) {
        SimpleDateFormat timeFormat = new SimpleDateFormat("HH:mm:ss a");
        SimpleDateFormat dateFormat = new SimpleDateFormat("EEEE, MMMM dd, yyyy");
        
        String currentTime = timeFormat.format(new Date());
        String currentDate = dateFormat.format(new Date());

        clockLabel.setText("<html>" + currentTime + "<br>" + currentDate + "</html>");
    }
}
