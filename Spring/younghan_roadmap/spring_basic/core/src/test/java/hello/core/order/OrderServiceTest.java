package hello.core.order;

import hello.core.AppConfig;
import hello.core.member.Grade;
import hello.core.member.domain.Member;
import hello.core.member.service.MemberService;
import hello.core.member.service.MemberServiceImpl;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class OrderServiceTest {

    //    MemberService memberService = new MemberServiceImpl(null);
//    OrderService orderService = new OrderServiceImpl(null, null);

    MemberService memberService;
    OrderService orderService;

    @BeforeEach
    void inject() {
        AppConfig appConfig = new AppConfig();
        memberService = appConfig.memberService();
        orderService = appConfig.orderService();
    }

    @Test
    void createOrder() {
        // given
        Member member = new Member(1L, "memberA", Grade.VIP);
        memberService.join(member);

        // when
        Order order = orderService.createOrder(member.getId(), "itemA", 10000);

        // then
        Assertions.assertThat(order.calculatePrice()).isEqualTo(9000);
    }
}
