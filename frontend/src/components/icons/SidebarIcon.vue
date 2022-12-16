<template>
  <div
    ref="lavContainer"
    :style="{
      overflow: 'hidden',
    }"
    @mouseenter="playAnimation"
    @focus="playAnimation"
    @blur="stopAnimation"
    @mouseleave="stopAnimation"
  />
</template>

<script>
import lottie from 'lottie-web'

export default {
  props: {
    json: {
      type: Object,
      required: true,
    },
    loop: {
      type: Boolean,
      default: true,
    },
  },

  mounted() {
    this.anim = lottie.loadAnimation({
      container: this.$refs.lavContainer,
      renderer: 'svg',
      animationData: this.json,
      autoplay: false,
      loop: this.loop,
    })
  },

  methods: {
    playAnimation() {
      this.anim.play()
    },
    stopAnimation() {
      this.anim.stop()
    },
  },
}
</script>
