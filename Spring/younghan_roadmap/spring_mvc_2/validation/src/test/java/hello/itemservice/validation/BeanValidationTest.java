package hello.itemservice.validation;

import hello.itemservice.domain.item.Item;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;

import javax.validation.ConstraintViolation;
import javax.validation.Validation;
import javax.validation.Validator;
import javax.validation.ValidatorFactory;
import java.util.Set;

import static org.assertj.core.api.Assertions.assertThat;

class BeanValidationTest {

    ValidatorFactory validatorFactory = Validation.buildDefaultValidatorFactory();
    Validator validator = validatorFactory.getValidator();

    @Test
    void beanValidation() {
        // given
        Item item = new Item();
        item.setItemName(" ");
        item.setPrice(100);
        item.setQuantity(1000000);

        // when
        Set<ConstraintViolation<Item>> validate = validator.validate(item);
        for (ConstraintViolation<Item> itemConstraintViolation : validate) {
            System.out.println("itemConstraintViolation = " + itemConstraintViolation);
        }

        // then
        assertThat(validate.size()).isEqualTo(3);
    }
}
