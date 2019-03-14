public class Follower implements Observer {
    private String followerName;

    public Follower(String name) {
        this.followerName = name;
    }

    public play() {
        System.out.println(this.followerName + " is playing a vid." );
    }

    @Override
    public void update(String s) {
        if(s == "play")
            this.play();
        else System.out.println(this.followerName + " " + s);
    }
}