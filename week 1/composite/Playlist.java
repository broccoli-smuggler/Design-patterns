import java.util.ArrayList;

public class Playlist implements IComponent {

    public String playlistName;
    public ArrayList<IComponent> playlist = new ArrayList();

    public Playlist(String playlistName) {
        this.playlistName = playlistName;
    }

    public void play() {
        for (IComponent component : playlist) {
            component.play();
        }
    }

    public void setPlaybackSpeed(float speed) {
        for (IComponent component : playlist) {
            component.setPlaybackSpeed(speed);
        }
    }

    public String getName() {
        return this.playlistName;
    }

    public int add(IComponent component) {
        this.playlist.add(component);
        return this.playlist.size() - 1;
    }

    public IComponent remove(int componentNumber) {
        return this.playlist.get[componentNumber];
    }
}