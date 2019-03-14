public class Program2 {
	public static void main(String args[]) {
        Channel channel = new Channel("live_watch", "stop");

        Follower j = new Follower("john");
        Follower b = new Follower("bim");

        channel.registerObserver(j);
        channel.setStatus("play");
        channel.setStatus("stop");

        channel.registerObserver(b);
        channel.setStatus("play");
        channel.unregisterObserver(j);
        channel.setStatus("stop");
	}
}