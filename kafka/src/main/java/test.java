import java.net.*;

public class test
{
    public static void outHostName(InetAddress address, String s)
    {
        System.out.println("通过" + s + "创建InetAddress对象");
        System.out.println("主 机 名:" + address.getCanonicalHostName());
        System.out.println("主机别名:" + address.getHostName());
        System.out.println("");
    }
    public static void main(String[] args) throws Exception
    {
        outHostName(InetAddress.getLocalHost(), "getLocalHost方法");
        outHostName(InetAddress.getByName("www.ibm.com"), "www.ibm.com");
        outHostName(InetAddress.getByName("aaaaaa.126.com"), "aaaaaa.126.com");
        outHostName(InetAddress.getByName("10.6.1.100"), "210.6.1.100");
        outHostName(InetAddress.getByName("10.6.1.103"), "10.6.1.103");
    }
}