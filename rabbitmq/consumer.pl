#!/usr/bin/perl
#
use Net::AMQP::RabbitMQ;
my $mq = Net::AMQP::RabbitMQ->new();
$mq->connect("localhost", { user => "guest", password => "guest" });
$mq->channel_open(1);
$mq->queue_declare(1, "foo");


while(1) {
    my $gotten = $mq->get(1, "foo");
    print $gotten->{body} . "\n";
}
$mq->disconnect();
