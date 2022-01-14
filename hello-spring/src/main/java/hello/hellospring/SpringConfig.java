package hello.hellospring;

import hello.hellospring.aop.TimeTraceAop;
import hello.hellospring.repository.*;
import hello.hellospring.service.MemberService;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.sql.Time;

@Configuration
public class SpringConfig {

  private final MemberRepository memberRepository;

  public SpringConfig(MemberRepository memberRepository) {
    this.memberRepository = memberRepository;
  }


  @Bean
  public MemberService memberService(){
    return new MemberService(memberRepository);
  }

//  @Bean
//  public MemberRepository memberRepository() {
//    return new MemoryMemberRepository();
//    return new JdbcMemberRepository(dataSource);
//    return new JdbcTemplateMemberRepository(dataSource);
//    return new JpaMemberRepository(em);
//  }


}
