#!/usr/bin/perl
#
use Net::AMQP::RabbitMQ;
my $mq = Net::AMQP::RabbitMQ->new();
$mq->connect("localhost", { user => "guest", password => "guest" });
$mq->channel_open(1);
$mq->queue_declare(1, "foo");

my $count = 0;
while(1) {
    $mq->publish(1, "foo", sprintf("Test message # %d", $count));
    $count++;
}
$mq->disconnect();
