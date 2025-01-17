<template>
  <div :class="['chips-wrapper', chipsType?.toLowerCase()]">
    <component
      v-if="chipsType"
      :is="`${chipsType}Icon`"
      :class="['icon', chipsType]"
    />
    <slot>
      <CustomText tag="span" :text="title" />
    </slot>
  </div>
</template>

<script>
import {capitalizeFirstLetter} from '@lib/utilities'

import maleIcon from '@components/icons/MaleIcon'
import femaleIcon from '@components/icons/FemaleIcon'
import SocialIcon from '@components/icons/SocialIcon'
import OnlineIcon from '@components/icons/OnlineIcon'
import TVRadioIcon from '@components/icons/TVRadioIcon'
import NegativeIcon from '@components/icons/NegativeIcon'
import PositiveIcon from '@components/icons/PositiveIcon'
import NeutralIcon from '@components/icons/NeutralIcon'
import TopicIcon from '@components/icons/HashtagIcon'
import CustomText from '@components/CustomText'

export default {
  name: 'BaseChips',
  components: {
    maleIcon,
    femaleIcon,
    SocialIcon,
    OnlineIcon,
    TVRadioIcon,
    NegativeIcon,
    PositiveIcon,
    NeutralIcon,
    TopicIcon,
    CustomText,
  },
  props: {
    chipsType: {type: String, default: ''},
  },
  computed: {
    title() {
      return this.currTitle(this.chipsType)
    },
  },
  methods: {
    capitalizeFirstLetter,
    currTitle(chipsTitle) {
      switch (chipsTitle) {
        case 'TVRadio':
          return 'TV&Radio'
        case 'Social':
          return 'Social Media'
        default:
          return capitalizeFirstLetter(chipsTitle)
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.chips-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;

  width: fit-content;
  height: fit-content;
  gap: 5px;
  padding: 6px 8px;

  border-radius: 2px 12px 12px 2px;
  background: var(--chips-background-secondary-color);

  overflow: hidden;
}

.male,
.doc {
  background: var(--chips-background-male-color);
}
.female,
.pdf {
  background: var(--chips-background-female-color);
}

.undefined {
  background: var(--background-additional-color);
}

.icon {
  width: 16px;
  height: 16px;
}

.tvradio {
  background: var(--background-additional-color);
}

.neutral {
  background-color: var(--neutral-secondary-color);
  color: var(--neutral-primary-color);
}

.positive {
  background-color: var(--positive-secondary-color);
  color: var(--positive-primary-color);
}

.negative {
  background-color: var(--negative-secondary-color);
  color: var(--negative-primary-color);
}
.topic {
  background-color: var(--hashtag-bg-color);
}
</style>
