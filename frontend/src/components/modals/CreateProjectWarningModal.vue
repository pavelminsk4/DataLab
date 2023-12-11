<template>
  <WarningModal @close="$emit('close')" @approve="$emit('approve')">
    <CustomText
      tag="div"
      text="After clicking the 'Continue' button, you will not be able to edit the
            project settings."
    />
    <CustomText
      tag="div"
      text="Please make sure that the keywords entered are correct."
    />
  </WarningModal>
</template>

<script>
import CustomText from '@components/CustomText'
import WarningModal from '@components/modals/WarningModal'

export default {
  name: 'CreateProjectWarningModal',
  components: {WarningModal, CustomText},
}
</script>
