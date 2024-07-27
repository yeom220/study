package jpabook.jpashop.service;

import jpabook.jpashop.domain.Member;
import jpabook.jpashop.repository.MemberRepository;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.transaction.annotation.Transactional;

@SpringBootTest
@Transactional
class MemberServiceTest {

    @Autowired
    MemberRepository memberRepository;
    @Autowired
    MemberService memberService;

    @Test
    void 회원가입() {
        // given
        Member member = new Member();
        member.setName("yeom");

        // when
        Long memberId = memberService.join(member);

        // then
        Assertions.assertThat(memberRepository.findOne(memberId)).isEqualTo(member);
    }

    @Test()
    void 중복_회원_예외() {
        //given
        Member memberA = new Member();
        memberA.setName("yeom");
        Member memberB = new Member();
        memberB.setName("yeom");

        // when
        memberService.join(memberA);

        // then
        Assertions.assertThatThrownBy(() -> memberService.join(memberB)).isInstanceOf(IllegalStateException.class);
    }

}