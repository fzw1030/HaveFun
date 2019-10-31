import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;

import java.util.Arrays;
import java.util.Properties;

public class KafkaConsumerDemo {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put("bootstrap.servers", "10.6.8.9:9001,10.6.8.9:9002,10.6.8.9:9003");
        String group="y";
        props.put("group.id", group);//指定消费者属于哪个组
        props.put("enable.auto.commit", "true");//开启kafka的offset自动提交功能，可以保证消费者数据不丢失
        props.put("auto.commit.interval.ms", "1000");
        props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
        String topic="mycp5-2";
        consumer.subscribe(Arrays.asList(topic));//指定消费的topic
        while (true) {
            ConsumerRecords<String, String> records = consumer.poll(100);
            for (ConsumerRecord<String, String> record : records)
                System.out.printf("group = %s ,topic = %s, offset = %d, partition =%d , timestamp= %s, key = %s, value = %s%n",
                        group,topic,record.offset(), record.partition(),record.timestamp(),record.key(), record.value());

        }
    }
}